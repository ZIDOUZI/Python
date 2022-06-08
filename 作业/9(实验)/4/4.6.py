l = list(input("请输入英文字符串:"))
while len(l) > 0:
    b = max(l)
    l.remove(b)
    print(b, end="")
