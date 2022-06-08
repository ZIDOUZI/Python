n = 0
for a in range(0, 101):
    for b in range(0, 51):
        c = 100 - 1 * a - 2 * b
        if c % 5 == 0 and c >= 0:
            n += 1
            print("{: 3d}, {: 3d}, {: 3d}".format(a, b, c // 5))
print(n)
