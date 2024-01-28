from functools import partial

from typing import Callable

def multiple_args(a = 1, b = 1, c = 1):
    return a * b *c

multiple_args_partial = partial(multiple_args, b = 2, c = 2)

def get_partial(fn: Callable) -> Callable | None:
    if isinstance(fn, partial):
        return fn.func
    return None