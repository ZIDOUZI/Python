import random

chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(0, 11):
    l = random.sample(chars, 8)
    password = "".join(l)
    print(password, end=", ")
