import random

a = random.randint(100, 999)
b = random.randint(100, 999)
c = random.randint(100, 999)
while a >= b:
    a, b = b, a
while a >= c:
    a, c = c, a
while b >= c:
    b, c = c, b
print(a, b, c)
