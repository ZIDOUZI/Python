with open("sy6-3.txt", "r", encoding="u8") as f:
    l = f.readlines()
    chinese = 0
    math = 0
    english = 0
    for i in l:
        chinese += int(i.split(",")[1])
        math += int(i.split(",")[2])
        english += int(i.split(",")[3])
    print("语文：{}".format(chinese / len(l)))
    print("数学：{}".format(math / len(l)))
    print("英语：{}".format(english / len(l)))