from car import Car
from motorcycle import Motorcycle
from truck import Truck

class Concessionaria:
    def __init__(self, nome):
        self.nome = nome
        self.vehicles = []

    def adicionar_veiculo(self, veiculo):
        self.vehicles.append(veiculo)

    def exibir_veiculos(self):
        print(f"Veículos disponíveis na concessionária {self.nome}:")
        for veiculo in self.vehicles:
            print(veiculo.display_info())