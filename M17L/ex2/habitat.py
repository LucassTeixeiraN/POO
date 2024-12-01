from animal import Animal

class Habitat:
    def __init__(self, tipo: str):
        self.tipo = tipo
        self.animais: list[Animal] = []

    def adicionar_animal(self, animal: Animal):
        if isinstance(animal, Animal):
            self.animais.append(animal)
            print(f"Animal {animal} adicionado ao habitat {self.tipo}.")
        else:
            print("Erro: O objeto não implementa a interface AnimalInterface.")

    def listar_animais(self):
        if not self.animais:
            print(f"O habitat {self.tipo} está vazio.")
        else:
            print(f"Animais no habitat {self.tipo}:")
            for animal in self.animais:
                print(f" - {animal}")
