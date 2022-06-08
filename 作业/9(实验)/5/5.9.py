def find(n):
    t = [1] * n
    c = 1
    while True:
        if n ** 3 == (c + n - 1) * n:
            for m in range(n):
                t[m] = c + m * 2
            return t
        c += 2


x = eval(input())
for i in range(x):
    print(i + 1, "**3=", sep="", end="")
    f = find(i + 1)
    for j in range(i):
        print(f[j], end="+")
    print(f[i])
