class Pneus:
            
    
    def __init__(self, direction, size, condition):
        if self.__directionVerify(direction):
            self.__direction = direction
        if self.__sizeVerify(size):
            self.__size = size
        if self.__conditionVerify(condition):
            self.__condition = condition

    @staticmethod
    def __directionVerify(direction):
        return -90 < direction < 90
    
    @staticmethod
    def __sizeVerify(size):
        return 13 < size < 20
    
    @staticmethod
    def __conditionVerify(condition):
        if condition.lower() in ["ruim", "bom", "excelente"]:
            return True

    #Getters
    def getDirection(self):
        return self.__direction

    def getSize(self):
        return self.__size

    def getCondition(self):
        return self.__condition

    # Setters
    def setDirection(self, direction):
        self.__direction = direction

    def setSize(self, size):
        self.__size = size

    def setCondition(self, condition):
        self.__condition = condition