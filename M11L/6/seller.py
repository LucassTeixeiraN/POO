from employee import Employee

class Seller(Employee):

    def __init__(self, name, cpf, rg, phone, type ,sectorCode, baseSalary, tax, valueSales, commission):
        super().__init__(name, cpf, rg, phone, type, sectorCode, baseSalary, tax)
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