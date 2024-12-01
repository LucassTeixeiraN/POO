from animal import Animal
from typing import Type

class Zoologico:
    def __init__(self):
        self.animais: list[Animal] = []

    def adicionar_animal(self, animal: Type[Animal]):
        if isinstance(animal, Animal):
            self.animais.append(animal)
        else:
            print("Erro: O objeto não é um animal válido.")

    def listar_animais(self):
        for animal in self.animais:
            print(animal)