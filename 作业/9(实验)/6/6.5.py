import random

with open("sy6-5.txt", "w") as f:
    for i in range(20):
        f.write(str(random.random()) + ", ")
        if i % 5 == 4:
            f.write("\n")
