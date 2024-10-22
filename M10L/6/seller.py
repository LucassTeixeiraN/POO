from employee import Employee

class Seller(Employee):

    def __init__(self, name, cpf, rg, phone, sectorCode, baseSalary, tax, valueSales, commission):
        super().__init__(name, cpf, rg, phone, sectorCode, baseSalary, tax)
        self.__valueSales = valueSales
        self.__commission = commission

    def getValueSales(self):
        return self.__valueSales
    
    def setValueSales(self, valueSales):
        self.__valueSales = valueSales

    def getCommission(self):
        return self.__commission
    
    def setCommission(self, commission):
        self.__commission = commission

    def calculateCommission(self):
        return self.getValueSales() * (self.getCommission()/100)

    def calculateSalary(self):
        return self.getBaseSalary() - (self.getTax()/100)*self.getBaseSalary() + self.calculateCommission()
    
    def showInfos(self):
        print(f"Informações do usuário:\nTipo de usuário: Vendedor\nNome: {self.getName()}\nCPF: {self.getCpf()}\nRG: {self.getRg()}\nTelefone: {self.getPhone()}")