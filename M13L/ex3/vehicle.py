from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    @abstractmethod # tipo vai ser alterado de acordo com as outras classes
    def vehicle_type(self):
        pass

    def display_info(self):
        return f"{self.vehicle_type()} - {self.brand} {self.model} ({self.year})"