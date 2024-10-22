from person import Person

class Employee(Person):
    
    def __init__(self, name, cpf, rg, phone, sectorCode, baseSalary, tax):
        super().__init__(name, cpf, rg, phone)
        self.__sectorCode = sectorCode
        self.__baseSalary = baseSalary
        self.__tax = tax

    def getSectorCode(self):
        return self.__sectorCode
    
    def setSectorCode(self, sectorCode):
        self.__sectorCode = sectorCode
        
    def getBaseSalary(self):
        return self.__baseSalary
    
    def setBaseSalary(self, baseSalary):
        self.__baseSalary = baseSalary

    def getTax(self):
        return self.__tax
    
    def setTax(self, tax):
        self.__tax = tax

    def calculateSalary(self):
        return self.getBaseSalary() - (self.getTax()/100)*self.getBaseSalary()
    
    def showInfos(self):
        print(f"Informações do usuário:\nTipo de usuário: Empregado\nNome: {self.getName()}\nCPF: {self.getCpf()}\nRG: {self.getRg()}\nTelefone: {self.getPhone()}")
