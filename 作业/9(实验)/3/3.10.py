for i in range(1, 1001):
    s = 0  # 因数和
    for j in range(1, i):
        if i % j == 0:
            s += j
    if s == i:
        print(s, end=",")


