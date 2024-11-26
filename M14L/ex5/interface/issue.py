from abc import ABC, abstractmethod

class Issue(ABC):
    @abstractmethod
    def get_issue(self):
        pass