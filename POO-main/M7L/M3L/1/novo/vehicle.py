# 1. Escreva uma classe chamada Vehicle que possua campos para a velocidade atual em
# km/h, a direção em graus dos pneus e o nome do proprietário. Crie métodos de
# acesso e impressão para esta classe e faça um programa de teste.

from modules import Person, Pneus, CurrentInformations

class Vehicle:

    def __init__(self, owner: Person, pneus: Pneus, currentInformations: CurrentInformations):
        self.__owner = owner
        self.__currentInformations = currentInformations
        self.__pneus = pneus

    def getOwnerInfos(self):
        print(f"Nome: {self.__owner.getName()}")
        print(f"Idade: {self.__owner.getAge()}")
        print(f"CPF: {self.__owner.getCPF()}")
    
    def getCurrentCarInfos(self):
        print(f"Velocidade: {self.__currentInformations.getVelocity()} km/h")
        print(f"Direção dos pneus: {self.__currentInformations.getDirection()}°")

    def getPneusInfos(self):
        print(f"Tamanho dos pneus: {self.__pneus.getSize()}")
        print(f"Condição dos pneus: {self.__pneus.getCondition()}")

    def changeOwnerInfos(self, name, age, cpf):
        self.__owner.setName(name)
        self.__owner.setAge(age)
        self.__owner.setCPF(cpf)

    def changePneusInfos(self, size, condition):
        self.__pneus.setSize(size) 
        self.__pneus.setCondition(condition)

    def changeCurrentInfos(self, velocity, direction):
        self.__currentInformations.setVelocity(velocity)
        self.__currentInformations.setPneusDirection(direction)
