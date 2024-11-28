from abc import ABC, abstractmethod

class ShowResults(ABC):
    @abstractmethod
    def showResults(self, type: str, value: float) -> str:
        pass