class Book:
    def __init__(self, id, name, amount):
        self.__id = id
        self.__name = name
        self.__amount = amount

    def getName(self):
        return self.__name
    
    def getAmount(self):
        return int(self.__amount)
    
    def getId(self):
        return self.__id
    
    def setName(self, name):
        self.__name = name

    def setAmount(self, amount):
        self.__amount = amount

    def setId(self, id):
        self.__id = id

    def __eq__(self, other: any):
        if self.getName() == other.getName():
            return True
        return False

    def __str__(self):
        return f"{self.getId()}. {self.getName()}: {self.getAmount()} unidades restantes"
    
