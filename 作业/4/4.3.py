s = input()
for i in set(s):
    print("'{}'出现了{}次".format(i, s.count(i)), end=", ")
