from math import *

for a in range(1, 1001):
    if (a ** 2 - a) % 10 ** ceil(log10(a + 1)) == 0:
        print(a, end=",")
    a += 1
