import jieba

with open("sy6-8.txt", "r", encoding="utf-8") as f:
    text = f.read()
    l = jieba.lcut(text)
    d = {}
    for i in set(l):
        d[i] = l.count(i)
    for i in sorted(d.items(), key=lambda x: x[1], reverse=True)[:5]:
        print("{} {}".format(i[0], i[1]))