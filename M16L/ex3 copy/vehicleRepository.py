from abc import ABC, abstractmethod

class VehicleRepository(ABC):
    @abstractmethod
    def save(self, vehicle):
        pass

    @abstractmethod
    def get_all(self):
        pass