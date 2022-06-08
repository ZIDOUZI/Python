from math import *

x1, y1, x2, y2 = eval(input("输入x1, y1, x2, y2: "))
print("距离是{:.2f}".format(sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)))
