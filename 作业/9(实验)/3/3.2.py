salary = eval(input("输入工资:"))
if salary > 1500:
    f = 0.03 * salary
elif salary > 800:
    f = 0.02 * salary
elif salary > 600:
    f = 0.015 * salary
elif salary > 400:
    f = 0.01 * salary
elif salary > 0:
    f = 0.05 * salary
else:
    f = -1
    exit(-1)
print("你需要支付 {.2f} 党费".format(f))
