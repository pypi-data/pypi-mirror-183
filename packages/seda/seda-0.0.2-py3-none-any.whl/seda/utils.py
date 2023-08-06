import functools
import importlib
import typing as t


@functools.lru_cache(maxsize=None)
def get_callable(path: str) -> t.Callable:
    mod_name, func_name = path.rsplit(".", 1)
    module = importlib.import_module(mod_name)
    func = getattr(module, func_name)

    if not callable(func):
        raise ValueError(f"'{path}' is not callable.")
    return func
