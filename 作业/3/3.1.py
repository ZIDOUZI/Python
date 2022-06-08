a = eval(input('购买金额:'))
if a >= 5000:
    print("{:.2f}".format(a * 0.85))
elif a >= 3000:
    print("{:.2f}".format(a * 0.9))
elif a >= 2000:
    print("{:.2f}".format(a * 0.95))
elif a >= 1000:
    print("{:.2f}".format(a * 0.95))
elif a > 0:
    print("{:.2f}".format(a))
else:
    print("???")
