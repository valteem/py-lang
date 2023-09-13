def bin(i: int, p: int) -> str:
    fmt = "{0:0" + str(p) + "b}"
    return fmt.format(i)

for i in range(8):
    print(bin(i, 4))

print("----")

for k in range(3):
    print(bin(1<<k, 4))