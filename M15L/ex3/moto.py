from interfaces import IMoto

class Moto(IMoto):
    def __init__(self, marca, modelo, ano, cilindrada):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cilindrada = cilindrada

    def registrar(self):
        print(f"Registrando moto: {self.marca} {self.modelo}, Ano: {self.ano}")

    def info_cilindrada(self):
        return f"Cilindrada: {self.cilindrada} cc"