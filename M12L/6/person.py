class Person:
    def __init__(self, name, address, paymentValue, contacts):
        self.__name = name
        self.__address = address
        self.paymentValue = paymentValue
        self.__contacts = contacts

    def doPayment(self):
        return self.paymentValue
    
    def showPersonalInfos(self):
        print(f"Nome: {self.__name}")
        print(f"Endereço: {self.__address}")
        print(f"Contatos: {self.__contacts}")
        print(f"Salário bruto: {self.doPayment()}")