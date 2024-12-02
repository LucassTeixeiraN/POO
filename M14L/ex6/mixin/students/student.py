from abc import ABC, abstractmethod
from .mixins import NotificationMixin

class Student(ABC, NotificationMixin):
    def __init__(self, nome):
        self.nome = nome
    
    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def estudar(self):
        pass
