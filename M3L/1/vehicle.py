# 1. Escreva uma classe chamada Vehicle que possua campos para a velocidade atual em
# km/h, a direção em graus dos pneus e o nome do proprietário. Crie métodos de
# acesso e impressão para esta classe e faça um programa de teste.

class Vehicle:

    def __init__(self, ownerName, velocity, pneusDirection):
        self.ownerName = ownerName
        self.velocity = velocity
        self.pneusDirection = pneusDirection
    
    def getOwnerName(self):
        return self.ownerName
    
    def getVelocity(self):
        return self.velocity
    
    def getPneusDirection(self):
        return self.pneusDirection

    def setOnwerName(self, ownerName):
        self.ownerName = ownerName

    def setVelocity(self, velocity):
        self.velocity = velocity

    def setPneusDirection(self, pneusDirection):
        self.pneusDirection = pneusDirection