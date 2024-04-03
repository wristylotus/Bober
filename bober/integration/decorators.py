from __future__ import annotations

import inspect
from functools import wraps, partial
from bober.manager import FOREST


def wood(func=None, *, name: str = None):
    if not name:
        raise ValueError('Argument "name" is required!')

    if not func:
        return partial(wood, name=name)

    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    __validate_name_usage(name)
    FOREST[name] = wrapper

    return wrapper


def __validate_name_usage(name: str) -> None:
    func = FOREST.get(name)
    if func:
        file_name = inspect.getfile(func)
        code_lines, _ = inspect.getsourcelines(func)
        preview_code = '            '.join(code_lines[:20])

        raise ValueError(f"""Wood with name '{name}' has already been planted here: {file_name}
                    {preview_code}
                    ......
                    ......
                """)
