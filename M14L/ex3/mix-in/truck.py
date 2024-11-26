from vehicle import Veiculo

class Caminhao(Veiculo):
    def __init__(self, marca, modelo, ano, capacidade_carga):
        super().__init__(marca, modelo, ano)
        self.capacidade_carga = capacidade_carga

    def tipo_veiculo(self):
        return "Caminhão"

    def exibir_info(self):
        return f"{super().exibir_info()}, Capacidade de Carga: {self.capacidade_carga}kg"