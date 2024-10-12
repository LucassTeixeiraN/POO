from person import Person

class Account:
    def __init__(self, client: Person, accountNumber, balance):
        self.__accountNumber = accountNumber
        self.__client = client 
        self.__balance = balance
        self.__client.setAccount(self)
    
    def getAccountNumber(self):
        return self.__accountNumber
    
    def getAccountOwnerName(self):
        return self.__client.getName()
    
    def getAccountOwnerDocument(self):
        return self.__client.getDocument()
    
    def getBalance(self):
        return self.__balance
    
    def changeBalance(self, balance):
        self.__balance += balance
    
    @staticmethod
    def amountVerify(amount):
        if amount > 0:
            return True
        return False
    
    @staticmethod
    def fundsVerify(amount, balance):
        if amount <= balance:
            return True
        return False
            
    
    def deposit(self, amount):
        if self.amountVerify(amount):
            self.__balance += amount

    def debit(self, amount):
        if self.amountVerify(amount) and self.fundsVerify(amount, self.account):
            self.changeBalance(amount*(-1))
        else:
            print("Insufficient funds")
        
    def displayAccount(self):
        print("-"*60)
        print(f"Nome: {self.getAccountOwnerName()}")
        print(f"Número da conta: {self.getAccountNumber()}")
        print(f"Saldo: {self.getBalance()}")
        print("-"*60)
        
        