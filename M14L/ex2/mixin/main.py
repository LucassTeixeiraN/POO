'''Implemente um sistema de Zoológico com sua classificação (mamífero, ave, réptil,
etc.), evidenciando a classe Animal como uma classe abstrata.'''
from animal import Ave, Mamifero, Reptil
from zoologico import Zoologico

def menu():
    print("\n===== Menu =====")
    print("1. Adicionar Mamífero")
    print("2. Adicionar Ave")
    print("3. Adicionar Réptil")
    print("4. Listar Animais")
    print("5. Sair")

    return input("Escolha uma opção (1-5): ")

def main():
    zoo = Zoologico()

    while True:
        escolha = menu()
        
        if escolha == '1':
            nome = input("Digite o nome do mamífero: ")
            mamifero = Mamifero(nome)
            zoo.adicionar_animal(mamifero)
            print(f"Mamífero {nome} adicionado com sucesso!")
        
        elif escolha == '2':
            nome = input("Digite o nome da ave: ")
            ave = Ave(nome)
            zoo.adicionar_animal(ave)
            print(f"Ave {nome} adicionada com sucesso!")
        
        elif escolha == '3':
            nome = input("Digite o nome do réptil: ")
            reptil = Reptil(nome)
            zoo.adicionar_animal(reptil)
            print(f"Réptil {nome} adicionado com sucesso!")
        
        elif escolha == '4':
            print("\nAnimais no Zoológico:")
            zoo.listar_animais()
        
        elif escolha == '5':
            print("Saindo do Zoológico...")
            break
        
        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 5.")

if __name__ == '__main__':
    main()