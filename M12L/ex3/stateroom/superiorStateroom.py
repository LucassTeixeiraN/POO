from ticket import VIP

class SuperiorStateRoom(VIP):
    def __init__(self, value, additional_value, location, superior_additional_value):
        super().__init__(value, additional_value)
        self.__location = location
        self._superior_additional_value = superior_additional_value

    def getValue(self):
        return self._value + self._additional_value + self._superior_additional_value

    def getLocation(self):
        return self.__location

    def printLocation(self):
        print(f"A localização do ingresso é: {self.__location}")