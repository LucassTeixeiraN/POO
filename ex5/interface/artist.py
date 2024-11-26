from abc import ABC, abstractmethod

class Artist(ABC):
    @abstractmethod
    def get_artist(self):
        pass