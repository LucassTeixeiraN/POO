
class Person:

    def __init__(self, name, age, cpf):
        self.__name = name
        self.__age = age
        self.__cpf = cpf

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def getCPF(self):
        return self.__cpf
    
    def setName(self, name):
        self.__name = name

    def setAge(self, age):
        self.__age = age

    def setCPF(self, cpf):
        self.__cpf = cpf
