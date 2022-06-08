a = 0
while 2 * a + 4 * (19 - a) != 44:
    a += 1
    if a < 0 or a > 19:
        break
else:
    print("鸡{}只, 兔{}只".format(a, 19 - a))
