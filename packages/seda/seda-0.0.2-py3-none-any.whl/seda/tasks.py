import inspect
import typing as t


class Task:
    def __init__(self, func: t.Callable) -> None:
        self.func = func
        self.path = inspect.getmodule(func).__name__  # type: ignore[union-attr]


class Schedule(Task):
    def __init__(
        self,
        func: t.Callable,
        expression: str,
        *,
        args: t.Optional[t.Sequence],
        kwargs: t.Optional[t.Dict[str, t.Any]],
    ) -> None:
        super().__init__(func)
        self.expression = expression
        self.args = args
        self.kwargs = kwargs
