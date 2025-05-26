from typing import Callable

def outer(a: int, b: int) -> Callable:
    def inner(x: int, y: int) -> int:
        return (a + b) * x + y
    return inner