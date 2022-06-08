l = input().split(",")
for s in l:
    if l.count(s) >= 2:
        print(True)
        break
else:
    print(False)
