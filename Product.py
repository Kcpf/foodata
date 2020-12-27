class Product:
    def __init__(self, name, description, image, price, category):
        self.name = name
        self.description = description
        self.image = image
        self.price = price
        self.complements = []
        self.category = category
    
    def getName(self):
        return self.name
    
    def setName(self, newName):
        self.name = newName
    
    def getDescription(self):
        return self.description
    
    def setDescription(self, newDescription):
        self.description = newDescription

    def getImage(self):
        return self.image
    
    def setImage(self, newImage):
        self.image = newImage

    def getPrice(self):
        return self.price
    
    def setPrice(self, newImage):
        self.price = newImage
    
    def getCategory(self):
        return self.category
    
    def setCategory(self, newCategory):
        self.category = newCategory

    def getComplements(self):
        return self.complements
    
    def addComplement(self, complement):
        self.complements.append(complement)