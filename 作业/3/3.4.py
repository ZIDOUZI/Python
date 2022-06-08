s = 0
n = eval(input(".."))
for i in range(1, 2 * n, 2):
    s += i * (-1) ** (i // 2)
