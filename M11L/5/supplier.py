from person import Person

class Supplier(Person):

    def __init__(self, name, cpf, rg, phone, type, valueCredit, valueDebt):
        super().__init__(name, cpf, rg, phone, type)
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

    @staticmethod
    def balanceVerify(credit, debit):
        if debit < credit:
            return True
        else:
            return False

    def getBalance(self):
        if self.balanceVerify(self.getValueCredit(), self.getValueDebit()):
            return self.getValueCredit() - self.getValueDebit()
        else:
            print("O usuário não possui saldo suficiente")