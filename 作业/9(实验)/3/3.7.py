for a in range(1, 1001):
    a1 = a % 10
    a2 = a // 10 % 10
    a3 = a // 100 % 10
    if a1 ** 3 + a2 ** 3 + a3 ** 3 == a:
        print(a, end=",")
    a += 1
