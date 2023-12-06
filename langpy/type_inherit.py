class A:
    def __init__(self, v):
        A.value = v
    def __eq__(self, other) -> bool:
        return isinstance(other, A) and self.value is other.value

class B(A):
    pass

def main():
    a = A(1)
    b = B(1)
    print(isinstance(b, A)) # isinstance() resolves inheritance
    print(type(a), type(b)) # type() returns immediate type
    print(a == b)


if __name__ == "__main__":
    main()