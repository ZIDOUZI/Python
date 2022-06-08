def sort_numbers(n):
    l0 = []
    while n != 0:
        l0.append(n % 10)
        n = n // 10
    l0.sort(reverse=True)
    num = 0
    for i in l0:
        num = num * 10 + int(i)
    return num


print(sort_numbers(1234321))
