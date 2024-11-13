from ticket import VIP

class LowerStateRoom(VIP):
    def __init__(self, valor, adicional, location):
        super().__init__(valor, adicional)
        self.__location = location

    def getLocation(self):
        return self.__location

    def printLocation(self):
        print(f"A localização do ingresso é: {self.__location}")