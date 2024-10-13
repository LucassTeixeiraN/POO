
class Person:

    def __init__(self, name, age, cpf):
        self.__name = name
        if self.ageVerify(age):
            self.__age = age

        if self.cpfVerify(cpf):
            self.__cpf = cpf


    @staticmethod
    def ageVerify(age):
        return age > 18
    
    @staticmethod
    def cpfVerify(cpf):
        return len(cpf) == 11

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
