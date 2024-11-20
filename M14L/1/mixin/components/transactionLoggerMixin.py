
class TransactionLoggerMixin:
    def transactionLog(self, amount, transationType):
        print(f"{transationType} de R${amount:.2f}")