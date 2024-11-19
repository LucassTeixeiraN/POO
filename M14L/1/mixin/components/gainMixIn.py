class GainMixIn:
    def calculateGain(self, time: int) -> float:
        return self.balance * ((1 + self.tax)**time)