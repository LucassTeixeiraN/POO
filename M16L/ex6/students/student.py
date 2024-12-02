from abc import ABC, abstractmethod

class Student(ABC):
    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def estudar(self):
        pass
