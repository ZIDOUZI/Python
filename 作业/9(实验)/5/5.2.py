from random import randint


def is_coprime(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a == 1


a, b = randint(1, 100), randint(1, 100)
print(a, b, is_coprime(a, b))
