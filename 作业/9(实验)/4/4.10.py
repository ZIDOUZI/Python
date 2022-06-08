scores = {"甲": 65, "乙": 97, "丙": 73, "丁": 85, "戊": 92}
a = list(zip(scores.values(), scores.keys()))
a = sorted(a, reverse=True)
for i in range(len(scores)):
    c = list(a[i])
    print(c[1])
