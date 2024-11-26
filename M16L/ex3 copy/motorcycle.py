from vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, engine_capacity):
        super().__init__(brand, model, year)
        self.engine_capacity = engine_capacity

    def vehicle_type(self):
        return "Moto"

    def display_info(self):
        return f"{super().display_info()}, Cilindrada: {self.engine_capacity}cc"