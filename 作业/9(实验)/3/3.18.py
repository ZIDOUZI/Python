h = 100
m = h
for i in range(1, 10):
    m += h / 2 ** i * 2
else:
    print("总经过{}米, 第10次反弹{}米".format(m, h / 2 ** (i + 1)))
