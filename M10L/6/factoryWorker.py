from employee import Employee

class FactoryWorker(Employee):

    def __init__(self, name, cpf, rg, phone, sectorCode, baseSalary, tax, valueProduction, commission):
        super().__init__(name, cpf, rg, phone, sectorCode, baseSalary, tax)
        self.__valueProduction = valueProduction
        self.__commission = commission

    def getValueProduction(self):
        return self.__valueProduction
    
    def setValueProduction(self, valueProduction):
        self.__valueProduction = valueProduction

    def getCommission(self):
        return self.__commission
    
    def setCommission(self, commission):
        self.__commission = commission

    def calculateCommission(self):
        return self.getValueProduction() * (self.getCommission()/100)

    def calculateSalary(self):
        return self.getBaseSalary() - (self.getTax()/100)*self.getBaseSalary() + self.calculateCommission()
    
    def showInfos(self):
        print(f"Informações do usuário:\nTipo de usuário: Trabalhador da Fábrica\nNome: {self.getName()}\nCPF: {self.getCpf()}\nRG: {self.getRg()}\nTelefone: {self.getPhone()}")