from typing import Any


class A(object):
    def __init__(self, _a) -> None:
        self.a = _a
    def __getattr__(self, attr):
        return 'Class has no `{}` attribute'.format(str(attr))
    def __getattribute__(self, attr) -> Any:
        if attr == 'c':
            print("A.c should always be 0")
            return 0
        else:
            return object.__getattribute__(self, attr) # using 'object' to avoid infinite recursion
    
def main():
    a = A(1)
    print(a.a)
    print(a.b)
    print(a.c)


if __name__ == "__main__":
    main()