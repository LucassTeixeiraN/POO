# 1. Escreva uma classe chamada Vehicle que possua campos para a velocidade atual em
# km/h, a direção em graus dos pneus e o nome do proprietário. Crie métodos de
# acesso e impressão para esta classe e faça um programa de teste.

from vehicle import Vehicle

def menu():
    while True:
        try:
            print("-"*60)
            option = int(input("Escolha uma opção:\n1- Registrar carro\n2- Ver carro registrado\n3- Editar carro registrado\n4- Sair\n"))
            print("-"*60)
            return option
        except ValueError:
            print("Valor inválido")
            menu()

def editionMenu():
        try:
            option = int(input("O que você deseja editar:\n1- Nome do propietário\n2- Velocidade do veículo\n3- Angulação dos pneus\n"))
            return option
        except ValueError:
            print("Valor inválido")
            editionMenu()
            
def registerCar():
    owner = input("Insira o nome do propietário do veículo: ")
    velocity = float(input("Insira a velocidade atual do carro (em km/h): "))
    pneusDirec = int(input("Insira a angulação dos pneus do carro: "))
    return Vehicle(owner, velocity, pneusDirec)
    
def editCar(obj):
    editingOption = editionMenu()
    if editingOption == 1:
        newOwner = input("Insira o nome do dono do veículo: ")
        obj.setOnwerName(newOwner)
    elif editingOption == 2:
        newVelocity = float(input("Insira a velocidade atual do carro (em km/h): "))
        obj.setVelocity(newVelocity)
    elif editingOption == 3:
        newDirection = int(input("Insira a angulação dos pneus do carro: "))
        obj.setPneusDirection(newDirection)
    else:
        print("Opção inválida")

def checkRegisteredCar(reg):
    if not reg:
        return True
    return False


def main():
    registeredCar = False
    while True:
        if input("Pressione ENTER para ver o menu") == "":
            option = menu()
            if option == 1:
                car = registerCar()
                registeredCar = True
                
            elif option == 2:
                if checkRegisteredCar(registeredCar):
                    print("Não há carros para mostrar")
                    continue
                car.__str__()

            elif option == 3:
                if checkRegisteredCar(registeredCar):
                    print("Não há carros para editar")
                    continue
                editCar(car)

            elif option == 4:
                print("Finalizando programa")
                break

            else:
                print("Opção inválida")
            
main()
