'''Implemente um sistema de Zoológico com sua classificação (mamífero, ave, réptil,
etc.), evidenciando a classe Animal como uma classe abstrata.'''
from animal import Ave, Mamifero, Reptil
from zoologico import Zoologico
from habitat import Habitat

def menu():
    print("\n===== Menu =====")
    print("1. Adicionar Habitat")
    print("2. Adicionar Animal a um Habitat")
    print("3. Listar Habitats e Animais")
    print("4. Sair")

    return input("Escolha uma opção (1-4): ")

def main():
    zoo = Zoologico()

    while True:
        escolha = menu()
        
        if escolha == '1':
            tipo = input("Digite o tipo do habitat (e.g., Savana, Floresta, Aquático): ")
            habitat = Habitat(tipo)
            zoo.adicionar_habitat(habitat)
        
        elif escolha == '2':
            if not zoo.habitats:
                print("Nenhum habitat disponível. Adicione um habitat primeiro.")
                continue
            
            print("Habitats disponíveis:")
            for idx, habitat in enumerate(zoo.habitats):
                print(f"{idx + 1}. {habitat.tipo}")

            habitat_escolhido = int(input("Escolha o habitat pelo número: ")) - 1
            if habitat_escolhido < 0 or habitat_escolhido >= len(zoo.habitats):
                print("Habitat inválido.")
                continue

            nome = input("Digite o nome do animal: ")
            tipo_animal = input("Digite o tipo do animal (Mamífero, Ave, Réptil): ").lower()

            if tipo_animal == "mamifero":
                animal = Mamifero(nome)
            elif tipo_animal == "ave":
                animal = Ave(nome)
            elif tipo_animal == "reptil":
                animal = Reptil(nome)
            else:
                print("Tipo de animal inválido.")
                continue

            zoo.habitats[habitat_escolhido].adicionar_animal(animal)
        
        elif escolha == '3':
            zoo.listar_habitats()
        
        elif escolha == '4':
            print("Saindo do Zoológico...")
            break
        
        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 4.")

if __name__ == '__main__':
    main()