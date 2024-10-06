# 1. Escreva uma classe chamada Vehicle que possua campos para a velocidade atual em
# km/h, a direção em graus dos pneus e o nome do proprietário. Crie métodos de
# acesso e impressão para esta classe e faça um programa de teste.

from vehicle import Vehicle
from modules import Person, Pneus, CurrentInformations

def menu():
    while True:
        try:
            print("-"*60)
            print("Escolha uma opção:")
            print("1- Registrar carro")
            print("2- Ver Informações do dono do veículo")
            print("3- Ver informações sobre a situação atual do carro")
            print("4- Ver informações sobre os pneus")
            print("5- Editar informações")
            print("6- Sair")
            option = int(input())
            print("-"*60)
            return option
        except ValueError:
            errorMessage()
            menu()

def editionMenu():
        try:
            option = int(input("O que você deseja editar:\n1- Informações do propietário\n2- Informações dos pneus\n3- Velocidade\n"))
            return option
        except ValueError:
            errorMessage()
            editionMenu()

def errorMessage():
    print("Valor inválido")

def setOwnerInfos():
    try:
        name = input("Insira o nome do dono do veículo: ")
        age = int(input("Insira a idade do dono do veículo: "))
        cpf = input("Insira o CPF do dono do veículo: ")
        return Person(name, age, cpf)
    except ValueError:
        errorMessage()
        setOwnerInfos()

def setPneusInfos():
    try:
        size = int(input("Insira o tamanho dos pneus: "))
        condition = input("Insira a condição dos pneus (ruim, boa ou excelente): ")
        return Pneus(size, condition)
    except ValueError:
        errorMessage()
        setPneusInfos()

def setCurrentInformations():
    try:
        velocity = float(input("Insira a velocidade atual do veículo (em km/h): "))
        direction = float(input("Insira a angulação dos pneus: "))
        return CurrentInformations(direction, velocity)
    except ValueError:
        errorMessage()
        setCurrentInformations()
            
def registerCar():
    owner = setOwnerInfos()
    pneus = setPneusInfos()
    velocity = setCurrentInformations()
    return Vehicle(velocity, owner, pneus)
    
def editCar(car):
    editingOption = editionMenu()
    if editingOption == 1:
        newOwnerInfos = setOwnerInfos()
        car.changeOwnerInfos(newOwnerInfos.getName(), newOwnerInfos.getAge(), newOwnerInfos.getCPF())
    elif editingOption == 2:
        newPneusInfos = setPneusInfos()
        car.changePneusInfos(newPneusInfos.getDirection(), newPneusInfos.getSize(), newPneusInfos.getCondition())
    elif editingOption == 3:
        newCurrentInformations = setCurrentInformations()
        car.changeCurrentInfos(newCurrentInformations)
    else:
        errorMessage()

def main():
    while True:
        try:
            if input("Pressione ENTER para ver o menu") == "":
                option = menu()
                if option == 1:
                    car = registerCar()
                elif option == 2:
                    car.getOwnerInfos()
                elif option == 3:
                    car.getCurrentCarInfos()
                elif option == 4:
                    car.getPneusInfos()
                elif option == 5:
                    editCar(car)
                elif option == 6:
                    print("Fechando programa")
                    break
                else:
                    errorMessage()

        except AttributeError:
            errorMessage()
main()

# tentar arrumar o except, ta saindo paia no terminal