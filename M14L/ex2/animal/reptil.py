from .animal import Animal

class Reptil(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def __str__(self):
        return f'Réptil: {self.nome}'

    def emitir_som(self):
        print(f'Som foi emitido pelo réptil "{self.nome}"')

    def comer(self, comida):
        print(f'O réptil "{self.nome}" comeu a comida: {comida}')
        