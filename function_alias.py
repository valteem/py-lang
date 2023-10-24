new_map = map

def f(iter):
    return new_map(lambda x: x*x, iter)

def main():
    l = [x/2. for x in range(5)]
    print(*f(l)) # https://stackoverflow.com/a/7731243

if __name__ == "__main__":
    main()
