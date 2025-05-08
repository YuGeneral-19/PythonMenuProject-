def show_menu():
    print("简易菜单")
    print("1. 选项一")
    print("2. 选项二")
    print("3. 退出")


def option1():
    print("执行选项一")


def option2():
    print("执行选项二")


def main():
    while True:
        show_menu()
        choice = input("请选择（1-3）：")
        if choice == '1':
            option1()
        elif choice == '2':
            option2()
        elif choice == '3':
            print("退出程序")
            break
        else:
            print("无效选择，请重新输入")


if __name__ == "__main__":
    main()