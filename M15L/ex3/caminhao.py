from interfaces import ICaminhao

class Caminhao(ICaminhao):
    def __init__(self, marca, modelo, ano, capacidade_carga):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.capacidade_carga = capacidade_carga

    def registrar(self):
        print(f"Registrando caminhão: {self.marca} {self.modelo}, Ano: {self.ano}")

    def info_capacidade_carga(self):
        return f"Capacidade de carga: {self.capacidade_carga} kg"