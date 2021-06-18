class Garnish(object):
    def __init__(self, garnish):
        self.id = garnish["id"]
        self.code = garnish["code"]
        self.description = garnish["description"]
        self.unit_price = garnish["unitPrice"]
        self.availability = garnish["availability"]
        self.tags = garnish["tags"]
        self.enabled = garnish["enabled"]