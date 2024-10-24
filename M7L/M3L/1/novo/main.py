# 1. Escreva uma classe chamada Vehicle que possua campos para a velocidade atual em
# km/h, a direção em graus dos pneus e o nome do proprietário. Crie métodos de
# acesso e impressão para esta classe e faça um programa de teste.

from vehicle import Vehicle
from person import Person
from pneus import Pneus

def errorMessage(msg):
    print(msg)

def intVerify(msg):
    try:
        number = int(input(msg))
        return number
    except ValueError:
        errorMessage("Valor inválido")
        return intVerify(msg)

def floatVerify(msg):
    try:
        number = float(input(msg))
        return number
    except ValueError:
        errorMessage("Valor inválido")
        return floatVerify(msg)

def menu():
    while True:
        print("-"*60)
        print("Escolha uma opção:")
        print("1- Registrar carro")
        print("2- Ver Informações do dono do veículo")
        print("3- Ver informações sobre a situação atual do carro")
        print("4- Ver informações sobre os pneus")
        print("5- Editar informações")
        print("6- Sair")
        option = input()
        print("-"*60)
        return option

def editionMenu():
    option = input("O que você deseja editar:\n1- Informações do propietário\n2- Informações dos pneus\n3- Velocidade\n")
    return option

def ageVerify(age):
    return age >= 18

def setOwnerInfos():
    name = input("Insira o nome do dono do veículo: ")
    age = intVerify("Insira a idade do dono do veículo: ")
    cpf = input("Insira o CPF do dono do veículo: ")
    if ageVerify(age):
        return Person(name, age, cpf)
    else:
        errorMessage("Valor inválido")
        setOwnerInfos()

def directionVerify(direction):
    return -90 <= direction <= 90

def sizeVerify(size):
    return 13 <= size <= 20

def conditionVerify(condition):
    if condition.lower() in ["ruim", "boa", "excelente"]:
        return True
    return False

def setPneusInfos():
    direction = floatVerify("Insira a angulação dos pneus (-90° a 90°): ")
    size = intVerify("Insira o tamanho dos pneus (13-20): ")
    condition = input("Insira a condição dos pneus (ruim, boa ou excelente): ")
    if directionVerify(direction) and sizeVerify(size) and conditionVerify(condition):
        return Pneus(direction, size, condition)
    else:
        errorMessage("Valor inválido")
        setPneusInfos()

def velocityVerify(vel):
    if vel >= 0:
        return True
    return False

def setVelocity():
    velocity = floatVerify("Insira a velocidade atual do veículo (em km/h): ")
    if velocityVerify(velocity):
        return velocity
    else:
        errorMessage("Valor inválido")
        setVelocity()
            
def registerCar():
    owner = setOwnerInfos()
    pneus = setPneusInfos()
    velocity = setVelocity()
    return Vehicle(velocity, owner, pneus)
    
def editCar(car):
    editingOption = editionMenu()
    if editingOption == '1':
        newOwnerInfos = setOwnerInfos()
        car.changeOwnerInfos(newOwnerInfos.getName(), newOwnerInfos.getAge(), newOwnerInfos.getCPF())
    elif editingOption == '2':
        newPneusInfos = setPneusInfos()
        car.changePneusInfos(newPneusInfos.getDirection(), newPneusInfos.getSize(), newPneusInfos.getCondition())
    elif editingOption == '3':
        newVelocity = setVelocity()
        car.setVelocity(newVelocity)
    else:
        errorMessage("valor inválido")
        editCar(car)

def main():
    car = None

    while True:
        if input("Pressione ENTER para ver o menu") == "":
            option = menu()
            if option == '1':
                car = registerCar()
            elif option == '2' and car != None:
                car.getOwnerInfos()
            elif option == '3' and car != None:
                car.getCurrentCarInfos()
            elif option == '4' and car != None:
                car.getPneusInfos()
            elif option == '5' and car != None:
                editCar(car)
            elif option == '6':
                print("Fechando programa")
                break
            else:
                errorMessage("Valor inválido")

main()
