from math import *

r = 2
s = pi * r ** 2 * 110 / 360 - r ** 2 * sin(radians(110)) / 2
print("{:.2f}".format(s))

