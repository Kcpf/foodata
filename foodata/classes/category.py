from foodata.classes.item import Item


class Category(object):
    def __init__(self, category):
        self.name = category["name"]
        self.code = category["code"]
        self.order = category["order"]
        self.enabled = category["enabled"]
        self.itens = [Item(i) for i in category["itens"]]
