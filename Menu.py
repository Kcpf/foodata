class Menu:
    def __init__(self):
        self.categories = []
    
    def addCategory(self, category):
        self.categories.append(category)
    
    def getCategories(self):
        return self.categories
    
    def getCategoriesNames(self):
        return [cat.name for cat in self.categories]
    
    def getProductsNamesByCategory(self):
        return {cat.name:cat.getProductsNames() for cat in self.categories}
    
    def getProductsNames(self, categoryIndex=None):
        if categoryIndex != None:
            return self.categories[categoryIndex].getProductsNames()
        else:
            return self.getProductsNamesByCategory()
    
    def getAllProducts(self):
        return sum([cat.getProducts() for cat in self.categories], [])
    
