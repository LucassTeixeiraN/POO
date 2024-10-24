class Pneus:
            
    
    def __init__(self, direction, size, condition):
        self.__direction = direction
        self.__size = size
        self.__condition = condition

    def getDirection(self):
        return self.__direction

    def getSize(self):
        return self.__size

    def getCondition(self):
        return self.__condition

    def setDirection(self, direction):
        self.__direction = direction

    def setSize(self, size):
        self.__size = size

    def setCondition(self, condition):
        self.__condition = condition