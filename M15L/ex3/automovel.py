
from interfaces import IAutomovel

class Automovel(IAutomovel):
    def __init__(self, marca, modelo, ano, capacidade_bateria):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.capacidade_bateria = capacidade_bateria

    def registrar(self):
        print(f"Registrando automóvel: {self.marca} {self.modelo}, Ano: {self.ano}")

    def info_bateria(self):
        return f"Capacidade da bateria: {self.capacidade_bateria} kWh"