from account import Account
class SavingsAccount(Account):
    RATE = 0.02

    def compute_interest(self):
        interest = self.balance * SavingsAccount.RATE
        self.deposit(interest)
        return interest