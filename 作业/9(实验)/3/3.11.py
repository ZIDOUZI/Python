from math import *

for i in range(2, 101):
    isPrime = True
    for x in range(2, ceil(sqrt(i)) + 1):
        if i % x == 0 and i != x:
            isPrime = False
    if isPrime:
        print(i, end=",")
