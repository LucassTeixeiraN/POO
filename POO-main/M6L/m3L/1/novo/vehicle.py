# 1. Escreva uma classe chamada Vehicle que possua campos para a velocidade atual em
# km/h, a direção em graus dos pneus e o nome do proprietário. Crie métodos de
# acesso e impressão para esta classe e faça um programa de teste.

from person import Person
from pneus import Pneus

class Vehicle:

    def __init__(self, velocity, owner: Person, pneus: Pneus):
        self.__owner = owner
        self.__velocity = velocity if velocity > 0 else 0
        self.__pneus = pneus

    def getOwnerInfos(self):
        print(f"Nome: {self.__owner.getName()}")
        print(f"Idade: {self.__owner.getAge()}")
        print(f"CPF: {self.__owner.getCPF()}")
    
    def getCurrentCarInfos(self):
        print(f"Velocidade: {self.__velocity} km/h")
        print(f"Direção dos pneus: {self.__pneus.getDirection()}°")

    def getPneusInfos(self):
        print(f"Tamanho dos pneus: {self.__pneus.getSize()}")
        print(f"Condição dos pneus: {self.__pneus.getCondition()}")

    def changeOwnerInfos(self, name, age, cpf):
        self.__owner.setName(name)
        self.__owner.setAge(age)
        self.__owner.setCPF(cpf)

    def changePneusInfos(self, direction, size, condition):
        self.__pneus.setDirection(direction) 
        self.__pneus.setSize(size) 
        self.__pneus.setCondition(condition)

    def setVelocity(self, velocity):
        self.__velocity = velocity
