x = input('输入数:')
while x != "quit":
    x = eval(x)
    if x % 5 == 0 and x % 7 == 0:
        print('x能同时被5和7整除')
    else:
        print('x不能同时被5和7整除')
    x = input('输入数:')
