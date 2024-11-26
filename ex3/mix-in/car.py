from vehicle import Veiculo
from mixins import MixinTetoSolar

class Automovel(Veiculo, MixinTetoSolar):
    def __init__(self, marca, modelo, ano, num_portas, possui_teto_solar):
        Veiculo.__init__(self, marca, modelo, ano)
        MixinTetoSolar.__init__(self, possui_teto_solar)
        self.num_portas = num_portas

    def tipo_veiculo(self):
        return "Automóvel"

    def exibir_info(self):
        return f"{super().exibir_info()}, Portas: {self.num_portas}, {self.info_teto_solar()}"