from .account import Account

class CurrentAccount(Account):
    def __init__(self, balance):
        super().__init__(balance)

    def update(self, tax):
        self._balance += self._balance * (tax * 2)