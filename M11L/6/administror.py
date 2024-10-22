from employee import Employee

class Administrator(Employee):

    def __init__(self, name, cpf, rg, phone, type, sectorCode, baseSalary, tax, subsistenceAllowance):
        super().__init__(name, cpf, rg, phone, type, sectorCode, baseSalary, tax)
        self.__subsistenceAllowance = subsistenceAllowance

    def getSubsistenceAllowance(self):
        return self.__subsistenceAllowance

    def setSubsistenceAllowance(self, subsistenceAllowance):
        self.__subsistenceAllowance = subsistenceAllowance
    
