def mul(*var):
    s = 1
    for i in var:
        s *= i
    return s


print(mul(1, 2, 3, 4, 5))
