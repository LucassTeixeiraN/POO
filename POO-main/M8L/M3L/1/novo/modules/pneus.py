class Pneus:

    def __init__(self, size, condition):
        self.__size = size
        self.__condition = condition

    #Getters
    def getSize(self):
        return self.__size

    def getCondition(self):
        return self.__condition

    # Setters
    def setSize(self, size):
        self.__size = size

    def setCondition(self, condition):
        self.__condition = condition