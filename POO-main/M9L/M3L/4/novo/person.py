from account import Account

class Person:
    def __init__(self, name, document):
        self.__name = name
        self.__document = document
        self.__account = None
        
    def getName(self):
     return self.__name
 
    def getDocument(self): 
        return self.__document
    
    def setAccount(self, account: Account):
       self.__account = account
    
    def getAccountNumber(self):
       return self.__account.getAccountNumber()