for i in range(1000, 10000):
    A = i % 10
    B = i // 10 % 10
    C = i // 100 % 10
    D = i // 1000 % 10
    if 1000 * A + 100 * B + 10 * C + D - 100 * C - 10 * D - C == 100 * A + 10 * B + C:
        print("{}{}{}{}".format(A, B, C, D))
