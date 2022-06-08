l = list(eval(input()))
s = 0
l.sort()
l.pop()
l.pop(0)
for i in l:
    s += i
print(s / len(l))
