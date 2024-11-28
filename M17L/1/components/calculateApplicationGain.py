from abc import ABC, abstractmethod

class CalculateApplicationGain(ABC):
    @abstractmethod
    def calculateGain(self, time):
        pass
