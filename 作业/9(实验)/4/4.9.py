account = {123456: "abcdefg"}

i = 2
while True:
    a = eval(input())
    if account.get(a) is None:
        print("账号不存在")
    else:
        b = input()
        if account.get(a) == b:
            print("Welcome!")
            break
        else:
            if i > 0:
                print("您还有{}次机会".format(i))
                i = i - 1
            else:
                print("无法登录")
                break
