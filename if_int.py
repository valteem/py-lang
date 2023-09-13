def bin(i: int) -> str:
    return "{0:04b}".format(i)

for i in range(8):
    for k in range(3):
        print(bin(i))
        print(bin(1<<k))
        print(bin(i & 1<<k))
        if i & 1<<k:
            print("append")
        print("----------")