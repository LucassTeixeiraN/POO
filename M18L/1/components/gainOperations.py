
class GainOperations:
    def calculateGain(self, balance: float, tax: float, time: int) -> float:
         return balance * ((1 + tax)**time)

    def calculateDifference(self, value:float, balance: float) -> float:
        return value-balance