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
            if 1 <= option <= 4:
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

def main():
    registeredCar = False
    while True:
        option = menu()
        if option == 1:
            owner = input("Insira o nome do propietário do veículo: ")
            velocity = float(input("Insira a velocidade atual do carro (em km/h): "))
            pneusDirec = float(input("Insira a angulação dos pneus do carro: "))
            car = Vehicle(owner, velocity, pneusDirec)
            registeredCar = True
        elif option == 2:
            print(f"Dono do carro: {car.getOwnerName()}")
            print(f"Velocidade atual do carro: {car.getVelocity()}")
            print(f"Angulação do pneu do carro: {car.getPneusDirection()}")
        elif option == 3:
            if registeredCar:
                editingOption = editionMenu()
                if editingOption == 1:
                    newOwner = input("Insira o nome do dono do veículo: ")
                    car.setOnwerName(newOwner)
                elif editingOption == 2:
                    newVelocity = float(input("Insira a velocidade atual do carro (em km/h): "))
                    car.setVelocity(newVelocity)
                elif editingOption == 3:
                    newDirection = float(input("Insira a angulação dos pneus do carro: "))
                    car.setPneusDirection(newDirection)
                else:
                    print("Opção inválida")

            else:
                print("Não há carros para editar")
        else:
            print("Finalizando programa")
            break
                    
            
main()