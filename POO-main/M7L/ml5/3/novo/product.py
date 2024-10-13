class Product:

    def __init__(self, name, price, amount):
        self.__name = name
        self.__price = price
        self.__amount = amount

    def getName(self):
        return self.__name
    
    def getPrice(self):
        return self.__price
    
    def getAmount(self):
        return self.__amount