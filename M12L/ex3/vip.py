from ticket import Ticket

class VIP(Ticket):
    def __init__(self, value, additional_value):
        self.__additional_value = additional_value
        super().__init__(value)

    def getValue(self):
        return self.__value + self.__additional_value