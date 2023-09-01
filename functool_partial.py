from functools import partial

def multiple_args(a = 1, b = 1, c = 1):
    return a * b *c

def main():
    single_arg = partial(multiple_args, b = 2, c = 2)
    print(single_arg(2))

if __name__ == "__main__":
    main()
