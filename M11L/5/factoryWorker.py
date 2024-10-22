from employee import Employee

class FactoryWorker(Employee):

    def __init__(self, name, cpf, rg, phone, type, sectorCode, baseSalary, tax, valueProduction, commission):
        super().__init__(name, cpf, rg, phone, type, sectorCode, baseSalary, tax)
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

    
