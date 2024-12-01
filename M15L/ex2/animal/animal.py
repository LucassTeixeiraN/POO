from abc import ABC, abstractmethod
from .comportamentos import EmitirSom, Comer

class Animal(ABC):
    def __init__(self, nome):
        self.nome = nome
    
    @abstractmethod
    def __str__(self):
        pass

Animal.register(EmitirSom)
Animal.register(Comer)
