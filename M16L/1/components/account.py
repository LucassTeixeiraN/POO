from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, name: str, document: str, accountNumber: str, balance: float, accountType: str):
        self.__name = name
        self.__document = document
        self.__accountNumber = accountNumber
        self.__balance = balance
        self.__accountType = accountType

    #Getters
    def getName(self) -> str:
        return self.__name

    def getDocument(self) -> str:
        return self.__document

    def getAccountNumber(self) -> str:
        return self.__accountNumber
    
    def getBalance(self) -> float:
        return self.__balance
    
    def getAccountType(self) -> str:
        return self.__accountType

    #Setters
    def setName(self, name:str) -> None:
        self.__name = name

    def setDocument(self, document:str) -> None:
        self.__document = document

    def setAccountNumber(self, accountNumber:str) -> None:
        self.__accountNumber = accountNumber

    def setBalance(self, balance:float) -> None:
        self.__balance = balance
    


    def checkBalance(self, value:float) -> bool:
        return self.__balance > value
    
    def deposit(self, value: float) -> None:
        self.setBalance(self.getBalance() + value)
        print("-"*60)

    @abstractmethod
    def showAccount(self):
        pass