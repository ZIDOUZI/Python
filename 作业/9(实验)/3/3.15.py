a, b, c = 1, 2, 3
n = 3
while c <= 2000:
    a, b, c = b, c, a + b + c
    n += 1
else:
    print(n)
