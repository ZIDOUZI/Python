def is_prime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    return True


a, b = eval(input("请输入两个整数："))
m = 0
for x in range(a, b + 1):
    if is_prime(x):
        if m != 0:
            print("+", end="")
        print("{}*{}".format(x, x), end="")
        m += x ** 2
print("={}".format(m))
