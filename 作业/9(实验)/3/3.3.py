from math import *

a, b, c = eval(input("请输入三条边, 数据间隔以逗号相隔: "))
if a <= 0 or b <= 0 or c <= 0:
    print("数据不合法!")
    exit(-1)
elif a + b <= c or b + c <= a or a + c <= b:
    print("不能构成三角形!")
    exit(-2)
else:
    h = (a + b + c) / 2
    s = sqrt(h * (h - a) * (h - b) * (h - c))
    print(s)
    