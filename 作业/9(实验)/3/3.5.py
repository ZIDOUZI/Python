from math import *

a, b, c = eval(input("输入a, b, c:"))
if a == 0 and b != 0:
    print("仅有一根: {}".format(-c / b))
elif a == 0 and b == 0:
    print("数据错误")
else:
    det = b ** 2 - 4 * a * c
    if det == 0:
        x1 = x2 = -b / 2 / a
    elif det > 0:
        x1, x2 = (-b + sqrt(det)) / 2 / a, (-b - sqrt(det)) / 2 / a
    else:
        x1, x2 = complex(-b, sqrt(-det)) / 2 / a, complex(-b, -sqrt(-det)) / 2 / a
    print(x1, x2)
