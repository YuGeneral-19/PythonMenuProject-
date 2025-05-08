import unittest
from unittest.mock import patch
from menu.menu import Menu
from menu.menu_item import MenuActionItem, MenuSubmenuItem


class TestMenu(unittest.TestCase):
    def setUp(self):
        self.menu = Menu("测试菜单")

    def test_add_item(self):
        item = MenuActionItem("测试选项", lambda: None)
        self.menu.add_item(item)
        self.assertIn(item, self.menu.items)

    @patch('builtins.input', side_effect=['1', 'q'])
    @patch('builtins.print')
    def test_execute(self, mock_print, mock_input):
        def test_action():
            print("测试操作")

        item = MenuActionItem("测试选项", test_action)
        self.menu.add_item(item)
        self.menu.execute()
        mock_print.assert_called_with("退出程序")

    def test_display(self):
        with patch('builtins.print') as mock_print:
            self.menu.display()
            mock_print.assert_called_with(f"{self.menu.name}菜单:")


if __name__ == '__main__':
    unittest.main()