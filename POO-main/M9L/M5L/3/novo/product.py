class Product:

    def __init__(self, name, price):
        self.__name = name
        self.__price = price
        self.__slot = None  

    def getName(self):
        return self.__name
    
    def getPrice(self):
        return self.__price
    
    def getSlot(self):
        return self.__slot
    
    def setSlot(self, slot):
        self.__slot = slot
