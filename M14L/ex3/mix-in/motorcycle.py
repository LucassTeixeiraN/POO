from vehicle import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindrada):
        super().__init__(marca, modelo, ano)
        self.cilindrada = cilindrada

    def tipo_veiculo(self):
        return "Moto"

    def exibir_info(self):
        return f"{super().exibir_info()}, Cilindrada: {self.cilindrada}cc"