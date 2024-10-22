class Person:

    def __init__(self, name, cpf, rg, phone, type):
        self.__name = name
        self.__cpf = cpf
        self.__rg = rg
        self.__phone = phone
        self.__type = type

    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name
        
    def getCpf(self):
        return self.__cpf
    
    def setCpf(self, cpf):
        self.__cpf = cpf

    def getRg(self):
        return self.__rg
    
    def setRg(self, rg):
        self.__rg = rg

    def getPhone(self):
        return self.__phone
    
    def setRg(self, phone):
        self.__phone = phone

    def getType(self):
        return self.__type
    
    def setType(self, type):
        self.__type = type

    def showInfos(self):
        print(f"Informações do usuário:\nTipo de usuário: {self.getType()}\nNome: {self.getName()}\nCPF: {self.getCpf()}\nRG: {self.getRg()}\nTelefone: {self.getPhone()}")