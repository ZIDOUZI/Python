s = 0
for i in range(2, 11, 2):
    t = 1
    for j in range(1, i + 1):
        t *= j
    s += t
print(s)
