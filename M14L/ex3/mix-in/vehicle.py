from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    @abstractmethod
    def tipo_veiculo(self):
        pass

    def exibir_info(self):
        return f"{self.tipo_veiculo()} - {self.marca} {self.modelo} ({self.ano})"