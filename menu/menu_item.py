class MenuItem:
    def __init__(self, name):
        self.name = name

    def trigger(self):
        pass


class MenuActionItem(MenuItem):
    def __init__(self, name, action):
        super().__init__(name)
        self.action = action

    def trigger(self):
        self.action()


class MenuSubmenuItem(MenuItem):
    def __init__(self, name, submenu):
        super().__init__(name)
        self.submenu = submenu

    def trigger(self):
        self.submenu.execute()