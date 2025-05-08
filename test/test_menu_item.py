import unittest
from unittest.mock import patch
from menu.menu_item import MenuActionItem, MenuSubmenuItem
from menu.menu import Menu


class TestMenuItem(unittest.TestCase):
    def test_menu_action_item(self):
        action_called = False

        def test_action():
            nonlocal action_called
            action_called = True

        item = MenuActionItem("测试选项", test_action)
        item.trigger()
        self.assertTrue(action_called)

    def test_menu_submenu_item(self):
        submenu = Menu("子菜单")
        item = MenuSubmenuItem("子菜单选项", submenu)
        with patch.object(submenu, 'execute') as mock_execute:
            item.trigger()
            mock_execute.assert_called_once()