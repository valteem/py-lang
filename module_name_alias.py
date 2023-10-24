from functools import partial

full = partial # magic

def func_1(a, b, c):
    return a + b + c

func_2 = full(func_1, b = 2, c = 3) # 'full for 'partial'

def main():
    print(func_2(1))


if __name__ == "__main__":
    main()