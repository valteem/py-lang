class A:
    def __init__(self, v):
        self.value = v
    def __eq__(self, other) -> bool:
        return isinstance(other, A) and self.value is other.value

class B(A):
    pass