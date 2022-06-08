from random import *

a, b = randint(100, 200), randint(100, 200)
print(a, b)
c = a * b
while a % b != 0:
    a, b = b, a % b
print("最大公因数是{}, 最小公倍数是{}".format(b, c // b))
