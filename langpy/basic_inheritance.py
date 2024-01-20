class A:
    def __init__(self):
        self.a = 1
        self.b = 2

class B(A):
    def __init__(self):
        super().__init__()
        self.c = 3