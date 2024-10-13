from account import Account

class Bank:
    #Essa classe possui uma dependência espalhada da classe Account

    def __init__(self):
        self.__accounts = []
        
    def addAccount(self, client: Account):
        self.__accounts.append(client)
        
    def clientByName(self, name):
        for client in self.__accounts:
            if client.getAccountOwnerName() == name:
                return client
    
    def clientByDocument(self, document):
        for client in self.__accounts:
            if client.getAccountOwnerDocument() == document:
                return client
    
    @staticmethod
    def decreaseBalance(account: Account, amount):
        account.debit(amount)
        
    @staticmethod
    def increaseBalance(account: Account, amount):
        account.changeBalance(amount)
        
    @staticmethod
    def accountInfos(account: Account):
        account.displayAccount()