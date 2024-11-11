from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, name, document, accountNumber, balance, accountType):
        self.__name = name
        self.__document = document
        self.__accountNumber = accountNumber
        self.__balance = balance
        self.__accountType = accountType

    def getName(self):
        return self.__name

    def getDocument(self):
        return self.__document

    def getAccountNumber(self):
        return self.__accountNumber
    
    def getBalance(self):
        return self.__balance
    
    def getAccountType(self):
        return self.__accountType

    def setName(self, name):
        self.__name = name

    def setDocument(self, document):
        self.__document = document

    def setAccountNumber(self, accountNumber):
        self.__accountNumber = accountNumber

    def setBalance(self, balance):
        self.__balance = balance
    
    def checkBalance(self, value):
        return self.__balance > value

    @abstractmethod
    def showAccount(self):
        pass