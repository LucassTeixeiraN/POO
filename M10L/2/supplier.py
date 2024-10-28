from person import Person

class Supplier(Person):

    def __init__(self, name, cpf, rg, phone, valueCredit, valueDebt):
        super().__init__(name, cpf, rg, phone)
        self.__valueCredit = valueCredit
        self.__valueDebt = valueDebt
        
    def getValueCredit(self):
        return self.__valueCredit
    
    def setValueCredit(self, value):
        self.__valueCredit = value

    def getValueDebit(self):
        return self.__valueDebt
    
    def setValueDebit(self, debit):
        self.__valueDebt = debit

    def getBalance(self):
        return self.getValueCredit() - self.getValueDebit()

    #Polimorfia
    def showInfos(self):
        print(f"Informações do usuário:\nTipo de usuário: Fornecedor\nNome: {self.getName()}\nCPF: {self.getCpf()}\nRG: {self.getRg()}\nTelefone: {self.getPhone()}")