from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def emitir_som(self):
        pass

    @abstractmethod
    def comer(self, comida):
        pass
