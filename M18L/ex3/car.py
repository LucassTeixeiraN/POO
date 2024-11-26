from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors

    def vehicle_type(self):
        return "Automóvel"

    def display_info(self):
        return f"{super().display_info()}, Portas: {self.num_doors}"