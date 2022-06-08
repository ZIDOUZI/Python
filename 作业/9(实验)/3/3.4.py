y, m = eval(input("请输入年份和月份,数据间以逗号相隔:"))
if m < 1 or m > 12 or y < 0:
    print("年份或者月份不合法!")
    exit(-1)
else:
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        print("{}年{}月有31天".format(y, m))
    elif m == 2:
        if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
            print("{}年{}月有29天".format(y, m))
        else:
            print("{}年{}月有28天".format(y, m))
    else:
        print("{}年{}月有30天".format(y, m))
