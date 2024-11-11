
class Bank:
    def __init__(self):
        self.__accounts = []

    def getAccouts(self):
        return self.__accounts

    def addAccount(self, account: any):
        self.__accounts.append(account)

    def findAccount(self, accountNumber):
        for i in self.__accounts:
            if i.getAccountNumber() == accountNumber:
                return i
        return None    
        

    