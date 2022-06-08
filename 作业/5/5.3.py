def odds(l):
    return [l[i] for i in range(len(l)) if i % 2 == 0]


print(odds([1, 2, 3, 4, 5]))
print(odds((7, 8, 9, 10, 12, 13)))
