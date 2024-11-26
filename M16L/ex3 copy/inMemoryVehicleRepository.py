from vehicleRepository import VehicleRepository

class InMemoryVehicleRepository(VehicleRepository):
    def __init__(self):
        self.vehicles = []

    def save(self, vehicle):
        self.vehicles.append(vehicle)

    def get_all(self):
        return self.vehicles