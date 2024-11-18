from abc import ABC, abstractmethod

class Student(ABC):
    def __init__(self, nome):
        self.nome = nome
    
    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def estudar(self):
        pass
