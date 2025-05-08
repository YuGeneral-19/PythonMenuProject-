class Menu:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def execute(self):
        while True:
            self.display()
            choice = input(f"请选择（1-{len(self.items)} 或输入 q 退出）：")
            if choice == 'q':
                print("退出程序")
                break
            try:
                item_index = int(choice) - 1
                if 0 <= item_index < len(self.items):
                    self.items[item_index].trigger()
                else:
                    print("无效选择，请重新输入")
            except ValueError:
                print("无效输入，请输入数字或 q 退出")

    def display(self):
        print(f"{self.name}菜单:")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.name}")