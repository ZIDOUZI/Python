from math import ceil


def is_symmetrical(x):
    for i in range(4):
        for j in range(4):
            if x[i][j] != x[j][i]:
                return False
    return True


def prime(num):
    if num <= 1:
        return False
    for i in range(2, ceil(num ** 0.5)):
        if num % i == 0:
            return False
    return True


if __name__ == '__main__':
    x = [input().split(" "), input().split(" "), input().split(" "), input().split(" ")]
    if is_symmetrical(x):
        print("The matrix is symmetrical")
    else:
        print("The matrix is not symmetrical")
    count = 0
    for m in range(4):
        for n in range(4):
            if prime(int(x[m][n])):
                count += 1
    print("The matrix has {} prime number(s)".format(count))
