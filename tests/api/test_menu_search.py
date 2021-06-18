from unittest import TestCase

from foodata.api.menu_search import MenuSearch

class TestMenuSearch(TestCase):

    def setUp(self):
        self.menu_searcher = MenuSearch()

    def test_menu_search(self):
        menu = self.menu_searcher.get_menu_from_restaurant("87e7c114-904d-43b9-a5cd-27135e46f89d")
    
        self.assertTrue(len(menu) != 0)
        self.assertTrue(type(getattr(menu[0], "name")) == str)
        