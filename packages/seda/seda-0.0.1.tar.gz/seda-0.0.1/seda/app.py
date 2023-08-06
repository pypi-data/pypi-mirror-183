import json
import logging
import typing as t
from collections import defaultdict

from mangum import Mangum
from mangum.types import LambdaContext, LambdaEvent

logger = logging.getLogger("seda")
logger.setLevel(logging.INFO)


class Seda(Mangum):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._event_handlers: t.Dict[str, t.List] = defaultdict(list)

    def __call__(self, event: LambdaEvent, context: LambdaContext) -> dict:
        data = {"event": event, "context": context.__dict__}
        logger.info(json.dumps(data, sort_keys=True, indent=4, default=str))

        if "event" in event:
            return {}
        return super().__call__(event, context)

    def schedule(self, expression: str, *args: t.Any, **kwargs: t.Any):
        def decorator(f):
            self._event_handlers["schedule"].append((f, args, kwargs))
            return f

        return decorator
