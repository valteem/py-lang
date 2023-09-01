# TODO: add support for default values of keyword arguments
# https://stackoverflow.com/questions/31728346/passing-default-arguments-to-a-decorator-in-python

def announce(text):
    def func_wrapper(f):
        def wrapper(*args, **kwargs):
            print(text)
            f(*args, **kwargs)
        return wrapper
    return func_wrapper

@announce(text = "multiplication")
def multiply(a = 1, b = 1):
    return a * b

def multiply_plain(a = 1, b = 1):
    return a * b

def main():
    print(multiply())       # returns None
    print(multiply_plain()) # returns 1

if __name__ == "__main__":
    main()
