ex = 1
x = eval(input("实数x:"))
n = 1
while True:
    m = x ** n
    n += 1
    for i in range(1, n):
        m /= i
    if -10 ** -6 < m < 10 ** -6:
        print(ex)
        break
    else:
        ex += m
