from account import Account
from typing import List

class Bank:
    def __init__(self):
        self.__accounts: List[Account] = []

    def getAccouts(self) -> List[Account]:
        return self.__accounts

    def addAccount(self, account: Account) -> None:
        self.__accounts.append(account)

    def findAccount(self, accountNumber:str) -> Account:
        for i in self.__accounts:
            if i.getAccountNumber() == accountNumber:
                return i
        return None    

    def findAccountByDocument(self, document: str) -> Account:
        for i in self.__accounts:
            if i.getDocument() == document:
                return i
        return None    
        

    