from vehicle import Veiculo
from interfaces import VeiculoEletrico, VeiculoTetoSolar

class Automovel(Veiculo, VeiculoEletrico, VeiculoTetoSolar):
    def __init__(self, marca, modelo, ano, num_portas, capacidade_bateria, possui_teto_solar):
        super().__init__(marca, modelo, ano)
        self.num_portas = num_portas
        self.capacidade_bateria = capacidade_bateria
        self.possui_teto_solar = possui_teto_solar

    def tipo_veiculo(self):
        return "Automóvel"

    def exibir_info(self):
        return f"{super().exibir_info()}, Portas: {self.num_portas}, {self.info_teto_solar()}, {self.exibir_info_bateria()}"

    def exibir_info_bateria(self):
        return f"Capacidade da Bateria: {self.capacidade_bateria}kWh"

    def info_teto_solar(self):
        return "Possui teto solar" if self.possui_teto_solar else "Não possui teto solar"