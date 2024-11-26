from abc import ABC, abstractmethod

class Author(ABC):
    @abstractmethod
    def get_author(self):
        pass