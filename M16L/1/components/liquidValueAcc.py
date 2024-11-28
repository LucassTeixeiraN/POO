from components import ShowResults, CalculateApplicationGain


class LiquidValueAcc(ShowResults, CalculateApplicationGain):

    def calculateGain(self, time: int) -> float:
         return self.getBalance() * ((1 + self.getTax())**time)

    def showResults(self, type, value):
        print(f"{type} de R${value:.2f} realizado")

    def calculateDifference(self, value):
        return value-self.getBalance()