class GainMixIn:
    def calculateGain(self, balance: float, tax: float, time: int) -> float:
        return balance * ((1 + tax)**time)