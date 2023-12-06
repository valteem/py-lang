# https://stackoverflow.com/questions/3277367/how-does-pythons-super-work-with-multiple-inheritance

class B1(object):
    def __init__(self):
        print("B1")

class B2(object):
    def __init__(self):
        print("B2")

class B3(B1, B2):
    def __init__(self):
        super(B3, self).__init__()
        print("B3")

class C1(object):
    def __init__(self):
        super(C1, self).__init__()
        print("C1")

class C2(object):
    def __init__(self):
        super(C2, self).__init__()
        print("C2")

class C3(C1, C2):
    def __init__(self):
        super(C3, self).__init__()
        print("C3")


def main():
    C3()
    B3()

if __name__ == "__main__":
    main()