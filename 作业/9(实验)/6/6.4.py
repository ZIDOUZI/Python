def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


with open("sy6-4.txt", "w") as f:
    for i in range(1, 101):
        if is_prime(i):
            f.write(str(i) + ", ")
