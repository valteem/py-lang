class CustomDivideByZeroException(Exception):
    def __init__(self, divisor, message="custom devide-by-zero exception"):
        self.message = message
        super().__init__(self.message)


def custom_divison(x, y):
    if y == 0:
        raise CustomDivideByZeroException(y)
    return x/y

def main():

    a = 1
    b = 0
    try:
        c = custom_divison(a, b)
    except CustomDivideByZeroException:
        c = "divide-by-zero error"

    print(f"custom division result is {c}")

if __name__ == "__main__":
    main()