with open("sy6-6.txt", "r", encoding="u8") as f:
    ll = f.readlines()
    d = {}
    for i in ll:
        name = i[0:i.find(" ")]
        l = sorted(eval(i[i.find(" ") + 1:-1].replace(" ", ","))[1:-1])
        d[name] = sum(l) / len(l)
    for (i, j) in sorted(d.items(), key=lambda x: x[1], reverse=True):
        print("{}的平均成绩是{:.2f}".format(i, j))
