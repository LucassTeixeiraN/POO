'''Implemente um sistema de Concessionária com os tipos de veículos (automóvel,
moto, caminhão, etc.), evidenciando a classe Vehicle como uma classe abstrata.'''

from car import Car
from motorcycle import Motorcycle
from truck import Truck

def main():
    vehicles = [
        Car("Toyota", "Corolla", 2021, 4),
        Motorcycle("Honda", "CB500", 2020, 500),
        Truck("Volvo", "FH", 2019, 18000)
    ]

    for vehicle in vehicles:
        print(vehicle.display_info())

if __name__ == "__main__":
    main()