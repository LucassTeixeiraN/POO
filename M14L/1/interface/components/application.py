from abc import abstractmethod, ABC

class Application(ABC):
    @abstractmethod
    def calculateGain(self, time):
        pass

    @abstractmethod
    def showResults(self):
        pass