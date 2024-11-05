from person import Person

class LegalPerson(Person):
    def __init__(self, name, address, paymentValue, contacts, cnpj, fantasyName, socialReason):
        super().__init__(name, address, paymentValue, contacts)
        self.__cnpj = cnpj
        self.__fantasyName = fantasyName
        self.__socialReason = socialReason
        self.__tax = 0.2

    def doPayment(self):
        return self.paymentValue * (1-self.__tax)

    def showPersonalInfos(self):
        print(f"CNPJ: {self. __cnpj}")
        print(f"Nome fantasia: {self. __fantasyName}")
        print(f"Razão social: {self. __socialReason}")
        print(f"Salário líquido: {self.doPayment()}")