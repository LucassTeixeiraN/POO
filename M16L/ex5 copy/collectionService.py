from abc import ABC, abstractmethod

class CollectionService(ABC):
    @abstractmethod
    def add_item(self, item):
        pass

    @abstractmethod
    def show_items(self):
        pass