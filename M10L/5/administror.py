from employee import Employee

class Administrator(Employee):

    def __init__(self, name, cpf, rg, phone, sectorCode, baseSalary, tax, subsistenceAllowance):
        super().__init__(name, cpf, rg, phone, sectorCode, baseSalary, tax)
        self.__subsistenceAllowance = subsistenceAllowance

    def getSubsistenceAllowance(self):
        return self.__subsistenceAllowance

    def setSubsistenceAllowance(self, subsistenceAllowance):
        self.__subsistenceAllowance = subsistenceAllowance

    # Polimorfismo
    def calculateSalary(self):
        return self.getBaseSalary() - (self.getTax()/100)*self.getBaseSalary() + self.getSubsistenceAllowance()
    
    # Polimorfismo
    def showInfos(self):
        print(f"Informações do usuário:\nTipo de usuário: Administrador\nNome: {self.getName()}\nCPF: {self.getCpf()}\nRG: {self.getRg()}\nTelefone: {self.getPhone()}")