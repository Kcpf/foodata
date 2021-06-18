from foodata.classes.garnish import Garnish


class Choice(object):
    def __init__(self, choice):
        self.code = choice["code"]
        self.name = choice["name"]
        self.min = choice["min"]
        self.max = choice["max"]
        self.order = choice["order"]
        self.availability = choice["availability"]
        self.garnish_itens = [Garnish(g) for g in choice["garnishItens"]]
        self.enabled = choice["enabled"]
