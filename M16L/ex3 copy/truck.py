from vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, brand, model, year, load_capacity):
        super().__init__(brand, model, year)
        self.load_capacity = load_capacity

    def vehicle_type(self):
        return "Caminhão"

    def display_info(self):
        return f"{super().display_info()}, Capacidade de Carga: {self.load_capacity}kg"