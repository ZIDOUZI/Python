with open("sy6-2.txt", "r") as f:
    muns = eval(f.read())
    print(max(muns), min(muns))
