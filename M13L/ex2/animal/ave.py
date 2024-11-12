from .animal import Animal

class Ave(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def __str__(self):
        return f'Ave: {self.nome}'

    def emitir_som(self):
        print(f'Som foi emitido pela ave "{self.nome}"')

    def comer(self, comida):
        print(f'A ave "{self.nome}" comeu a comida: {comida}')