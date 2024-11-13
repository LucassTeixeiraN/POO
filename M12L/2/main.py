'''Implemente o diagrama de classes abaixo:'''
from cat import Cat
from dog import Dog
from animal import Animal

def menu():
    print("1. Adicionar animal")
    print("2. Ver animal")
    print("3. Comportamento do animal")
    print("0. Sair")

    return input("Escolha uma opção: ")

def animalCreateMenu():
    print("Selecione o animal")
    print("1. Cachorro")
    print("2. Gato")
    
    return input("Escolha o animal: ")

def createAnimal():
    choice = animalCreateMenu()
    name = input("Nome: ")
    breed = input("Raça: ")
    if choice == "1":
        animal = Dog(name)
    elif choice == "2":
        animal = Cat(name)
    else:
        print("Opção inválida")
        return createAnimal()
    animal.setBreed(breed)
    return animal


def main():
    animal = None

    while True:
        option = menu()

        if option == "1":
            animal = createAnimal()
        elif option == "2" and animal:
            print(f"Nome do animal: {animal.getName()}")
            print(f"Raça do animal: {animal.getBreed()}")
        elif option == "3" and animal:
            animal.walk()
        elif option == "0":
            print("Saindo....")
            break
        else:
            print("Opção inválida")

main()