from .animal import Animal

class Mamifero(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def __str__(self):
        return f'Mamífero: {self.nome}'

    def emitir_som(self):
        print(f'Som foi emitido pelo mamifero "{self.nome}"')

    def comer(self, comida):
        print(f'O mamifero "{self.nome}" comeu a comida: {comida}')