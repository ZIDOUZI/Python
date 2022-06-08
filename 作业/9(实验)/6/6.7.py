d = {}
with open("sy6-7.txt", "r", encoding="utf-8") as f:
    for line in f:
        name, email = line.split(",")
        d[name] = email

while True:
    name = input("请输入姓名：")
    if name == "":
        break
    if name in d:
        print(d[name])
    else:
        print("没有找到")
