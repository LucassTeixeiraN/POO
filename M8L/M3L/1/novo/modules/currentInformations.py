class CurrentInformations:

    def __init__(self, pneusDirection, velocity):
        self.__pneusDirection = pneusDirection
        self.__velocity = velocity

    def getVelocity(self):
        return self.__velocity
    
    def getPneusDirection(self):
        return self.__pneusDirection
    
    def setVelocity(self, velocity):
        self.__velocity = velocity

    def setPneusDirection(self, direction):
        self.__pneusDirection = direction 