

w = eval(input("输入行李重量(kg):"))
if w > 50:
    y = 50 * 0.25 + (w - 50) * 0.35
elif w > 0:
    y = w * 0.25
else:
    print("error")
    y = -1
    exit(-1)
print("你的费用是: {}".format(y))
