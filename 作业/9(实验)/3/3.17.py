a = eval(input("输入a:"))
if a < 0:
    exit(0x0001)
xn = a
xn1 = (a + 1) / 2
while xn1 - xn > 10 ** -6 or xn1 - xn < -10 ** -6:
    xn, xn1 = xn1, (xn1 + a / xn1) / 2
else:
    print(xn)
