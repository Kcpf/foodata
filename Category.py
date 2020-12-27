class Category:
    def __init__(self, name):
        self.name = name
        self.products = []
    
    def getName(self):
        return self.name
    
    def setName(self, newName):
        self.name = newName
    
    def addProduct(self, product):
        self.products.append(product)
    
    def getProducts(self):
        return self.products
    
    def getProductsNames(self):
        return [prod.name for prod in self.products]
    