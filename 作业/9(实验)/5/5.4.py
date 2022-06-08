dic = {}


def add_dic():
    e = input("please input an English word:")
    dic[e] = input("please input the Chinese meaning:")


def search_dic():
    e = input("please input the word you want to look for:")
    return e, dic[e]


while True:
    choice = input("choose 1-input,2-look for,3-exit\n")
    if choice == "1":
        add_dic()
    elif choice == "2":
        print(" ".join(search_dic()))
    elif choice == "3":
        break
    else:
        print("invalid choice")
