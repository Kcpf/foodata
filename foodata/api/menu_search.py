import requests

from foodata.api.helpers import headers_second, payload
from foodata.classes.category import Category


class MenuSearch(object):
    def __init__(self):
        self.menu = None
    
    def _menu_search(self, merchant_id):
        url = f"https://wsloja.ifood.com.br/ifood-ws-v3/restaurants/{merchant_id}/menu"

        try:
            response = requests.request("GET", url, headers=headers_second, data=payload).json()
            self.menu = response["data"]["menu"]
        except Exception:
            raise Exception("A problem has ocurred during Menu Search Request")
    
    def get_menu_from_restaurant(self, merchant_id = None):
        assert merchant_id != None

        self._menu_search(merchant_id)
        menu = [Category(cat) for cat in self.menu]

        return menu
