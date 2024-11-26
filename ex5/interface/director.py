from abc import ABC, abstractmethod

class Director(ABC):
    @abstractmethod
    def get_director(self):
        pass