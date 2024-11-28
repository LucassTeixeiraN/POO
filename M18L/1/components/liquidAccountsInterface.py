from abc import ABC, abstractmethod

class LiquidAccountsInterface(ABC):
    @abstractmethod
    def estimateGain(self, time: int) -> None:
        pass