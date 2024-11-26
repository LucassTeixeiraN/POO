from abc import ABC, abstractmethod

class Collection(ABC):
    def __init__(self, title, year):
        self.title = title
        self.year = year

    @abstractmethod
    def get_info(self):
        pass