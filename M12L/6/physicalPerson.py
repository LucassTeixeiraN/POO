from person import Person

class PhysicalPerson(Person):
    def __init__(self, name, address, paymentValue, contacts, cpf):
        super().__init__(name, address, paymentValue, contacts)
        self.__cpf = cpf
        self.__tax = 0.1

    def doPayment(self):
        return self.paymentValue - self.paymentValue*self.__tax

    def showPersonalInfos(self):
        print(f"CPF: {self. __cpf}")
        print(f"Salário líquido: {self.doPayment()}")