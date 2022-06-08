from random import *

while True:
    a, b = randint(-9, 10), randint(-9, 10)
    answer = eval(input("{} + {} = ".format(a, b)))
    if answer == eval("quit"):
        break
    elif answer != (a + b):
        print("计算错误")
    else:
        print("计算正确")

