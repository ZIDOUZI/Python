import math

r, h = eval(input("输入r, h"))
S = 2 * math.pi * r * h + 2 * math.pi * r ** 2
V = math.pi * r ** 2 * h

print("圆柱的表面积为{0:f}, 体积为{1:f}".format(S, V))

