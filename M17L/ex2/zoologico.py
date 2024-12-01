from habitat import Habitat

class Zoologico:
    def __init__(self):
        self.habitats: list[Habitat] = []

    def adicionar_habitat(self, habitat: Habitat):
        self.habitats.append(habitat)
        print(f"Habitat {habitat.tipo} adicionado ao zoológico.")

    def listar_habitats(self):
        if not self.habitats:
            print("O zoológico ainda não possui habitats.")
        else:
            for habitat in self.habitats:
                print(f"Habitat: {habitat.tipo}")
                habitat.listar_animais()
                