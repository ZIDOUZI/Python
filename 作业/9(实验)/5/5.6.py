from math import ceil


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, ceil(num ** 0.5)):
        if num % i == 0:
            return False
    return True


n = 1
for j in range(4, 1000, 2):
    for k in range(2, j // 2):
        if is_prime(j - k) and is_prime(k):
            print(j, "=", j - k, "+", k, sep="", end=",\t\t")
            if n == 6:
                print()
                n = 0
            n += 1
            break
