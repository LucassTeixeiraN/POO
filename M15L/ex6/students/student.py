from abc import ABC, abstractmethod

class Student(ABC):
    @abstractmethod
    def __str__(self):
        pass

class Study(ABC):
    @abstractmethod
    def estudar(self):
        pass

Student.register(Study)