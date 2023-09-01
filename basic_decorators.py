def announce(text):
    def func_wrapper(f):
        def wrapper(*args, **kwargs):
            print(text)
            return f(*args, **kwargs)
        return wrapper
    return func_wrapper

@announce(text = "multiplication")
def multiply(a = 1, b = 1):
    return a * b

def main():
    print(multiply())
    print(multiply(2, 4))

if __name__ == "__main__":
    main()
