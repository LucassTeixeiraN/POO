from components import ShowResults


class FixedValueAcc(ShowResults):

    def showResults(self, type, value):
        print(f"{type} de R${value:.2f} realizado")