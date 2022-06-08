s = 0
n = eval(input("输入上限n:"))
for a in range(1, n + 1):
    s1 = 0
    b = 1
    while b <= a:
        s1 += b
        b += 1
    s += s1
    a += 1
print(s)
