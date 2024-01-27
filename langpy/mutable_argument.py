class A:
    def __init__(self) -> None:
        self.x = 1

def function_with_mutable_arg(a = A()):
    a.x *= 2
    return a.x