class TransferMixIn:

    def transfer(self, value):
        self.setBalance(self.balance-value)