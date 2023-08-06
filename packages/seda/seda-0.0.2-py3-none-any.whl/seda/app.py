import asyncio
import inspect
import shlex
import subprocess
import typing as t

from mangum import Mangum
from typing_extensions import Literal

from seda import types
from seda.tasks import Schedule, Task
from seda.utils import get_callable


class Seda:
    def __init__(
        self,
        app: t.Callable,
        *,
        lifespan: Literal["auto", "on", "off"] = "auto",
        api_base_path: str = "/",
        default_handler: t.Optional[t.Callable] = None,
        schedules: t.Optional[t.Sequence[Schedule]] = None,
        **options: t.Any,
    ) -> None:
        self.app = app
        self.lifespan = lifespan
        self.api_base_path = api_base_path
        self.tasks: t.List[Task] = []
        self.schedules = [] if schedules is None else list(schedules)

        if default_handler is None:
            self.default_handler: t.Callable = Mangum(
                self.app,
                lifespan=self.lifespan,
                api_gateway_base_path=self.api_base_path,
                **options,
            )
        else:
            self.default_handler = default_handler

    def __call__(self, event: types.Event, context: types.Context) -> t.Any:
        if "python" in event:
            return exec(event["python"])
        elif "cmd" in event:
            subprocess.run(shlex.split(event["cmd"]))
            return
        elif "task" in event:
            return self.run_task(event, context)
        return self.default_handler(event, context)

    def run_task(self, event: types.Event, context: types.Context) -> t.Any:
        data = event["task"]
        func = get_callable(data["path"])
        args = data.get("args", ())
        kwargs = data.get("kwargs", {})
        sig = inspect.signature(func)

        # TODO: fix f(event, x) & f(event, /) ??
        if "event" in sig.parameters:
            kwargs.setdefault("event", event)
        if "context" in sig.parameters:
            kwargs.setdefault("context", context)

        f = func(*args, **kwargs)
        if asyncio.iscoroutinefunction(func):
            return asyncio.run(f)
        return f

    def task(self) -> t.Callable:
        # TODO: add SNS/SQS call
        def decorator(f: t.Callable) -> t.Callable:
            self.tasks.append(Task(f))
            return f

        return decorator

    def schedule(
        self,
        expression: str,
        *,
        args: t.Optional[t.Sequence] = None,
        kwargs: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> t.Callable:
        def decorator(f: t.Callable) -> t.Callable:
            task = Schedule(f, expression, args=args, kwargs=kwargs)
            self.schedules.append(task)
            return f

        return decorator
