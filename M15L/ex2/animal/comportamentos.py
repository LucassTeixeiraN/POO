from abc import ABC, abstractmethod

class EmitirSom(ABC):
    @abstractmethod
    def emitir_som(self):
        pass

class Comer(ABC):
    @abstractmethod
    def comer(self, comida):
        pass
