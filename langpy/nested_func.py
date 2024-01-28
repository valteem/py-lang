def outer(a: int, b: int) -> callable:
    def inner(x: int, y: int) -> int:
        return (a + b) * x + y
    return inner