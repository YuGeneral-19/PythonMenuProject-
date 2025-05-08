from menu import Menu, MenuActionItem, MenuSubmenuItem


def action1():
    print("执行选项一操作")


def action2():
    print("执行选项二操作")


def action3():
    print("执行选项三操作")


if __name__ == "__main__":
    # 创建子菜单
    submenu = Menu("子菜单")
    submenu.add_item(MenuActionItem("子选项1", action3))

    # 创建主菜单
    main_menu = Menu("主菜单")
    main_menu.add_item(MenuActionItem("选项一", action1))
    main_menu.add_item(MenuActionItem("选项二", action2))
    main_menu.add_item(MenuSubmenuItem("子菜单", submenu))

    main_menu.execute()