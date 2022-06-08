def count_num(s):
    dic = {}
    for i in s.split(" "):
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    return dic


s1 = "python java php c++ c c# javascript vb vfp vbscript c++ c#"
dic = count_num(s1)
print("Order of keys:")
for i in sorted(dic.items(), key=lambda x: x[0]):
    print(i[0], i[1])
print("Order of values:")
for i in sorted(dic.items(), key=lambda x: x[1]):
    print(i[0], i[1])
