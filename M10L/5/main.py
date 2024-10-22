'''Implemente a classe FactoryWorker como subclasse da classe Employee. Um
determinado operário tem como atributos, para além dos atributos da classe Person e
da classe Employee, o atributo valueProduction (que corresponde ao valor monetário
dos artigos efetivamente produzidos pelo operário) e commission (que corresponde à
porcentagem do valueProduction que será adicionado ao vencimento base do
operário). Note que deverá redefinir nesta subclasse o método herdado
calculateSalary (o salário de um operário é equivalente ao salário de um empregado
usual acrescido da referida comissão). Altere o main para que você possa verificar o
funcionamento dos métodos implementados na classe FactoryWorker e os herdados.'''

from person import Person
from supplier import Supplier
from employee import Employee
from administror import Administrator
from factoryWorker import FactoryWorker

user: Person = None
supplier: Supplier = None
employee: Employee = None
administrator: Administrator = None
factWorker: FactoryWorker = None

def ErrorMessage(err):
    print(err)

def floatVerify(message):
    try:
        number = float(input(message))
        return number
    except:
        ErrorMessage("Valor Inválido")
        return floatVerify(message)

def intVerify(message):
    try:
        number = int(input(message))
        return number
    except:
        ErrorMessage("Valor Inválido")
        return floatVerify(message) 

# Comun user functions
def userRegister():
    print("Insira as seguintes informações do usuário: ")
    name = input("Name: ")
    cpf = input("Cpf: ")
    rg = input("Rg: ")
    phone = input("Phone: ")
    return name, cpf, rg, phone

def comumUserMenu():
    while True:
        print("1. Registrar usuário")
        print("2. Ver informações do usuário")
        print("0. Voltar")
        option = input("Opção: ")
        return option

def userActions(opt):
    global user
    
    if opt == "1":
        name, cpf, rg, phone = userRegister()
        user = Person(name, cpf, rg, phone)
    elif opt == "2":
        print("-"*60)
        user.showInfos()
        print("-"*60)
    elif opt == "0":
        print("-"*60)
        main()
    else:
        print("-"*60)
        ErrorMessage("Opção inválida")

# Supplier Functions
def supplierMenu():
    while True:
        print("1. Registrar fornecedor")
        print("2. Ver informações do fornecedor")
        print("3. Ver saldo do fornecedor")
        print("0. Voltar")
        option = input("Opção: ")
        return option

def getSupplierInfos():
    credit = floatVerify("Crédito: ")
    debit = floatVerify("Débito: ")
    if credit >= 0 and debit >= 0:
        return credit, debit
    else:
        ErrorMessage("Valores inválidos")
        return getSupplierInfos()


def supplierActions(opt):
    global supplier

    if opt == "1":
        name, cpf, rg, phone = userRegister()
        credit, debit = getSupplierInfos()
        supplier = Supplier(name, cpf, rg, phone, credit, debit)

    elif opt == "2":
        print("-"*60)
        supplier.showInfos()
        print("-"*60)
    elif opt == "3":
        print("-"*60)
        print("Saldo:", supplier.getBalance())
        print("-"*60)
    elif opt == "0":
        print("-"*60)
        main()
    else:
        print("-"*60)
        ErrorMessage("Opção inválida")

#Employee Functions
def employeeMenu():
    while True:
        print("1. Registrar funcionário")
        print("2. Ver informações do funcionário")
        print("3. Ver salário líquido")
        print("0. Voltar")
        option = input("Opção: ")
        return option
    
def getEmployeeInfos():
    sectorCode = intVerify("Código do setor: ")
    baseSalary = floatVerify("Base salarial: ")
    tax = floatVerify("Impostos (em porcentagem): ")
    
    if sectorCode > 0 and baseSalary > 0 and 0 <= tax < 100:
        return sectorCode, baseSalary, tax
    else:
        ErrorMessage("Valores inválidos")
        return getEmployeeInfos()

def employeeActions(opt):
    global employee

    if opt == "1":
        name, cpf, rg, phone = userRegister()
        sectorCode, baseSalary, tax = getEmployeeInfos()
        employee = Employee(name, cpf, rg, phone, sectorCode, baseSalary, tax)
    elif opt == "2":
        print("-"*60)
        employee.showInfos()
        print("-"*60)
    elif opt == "3":
        print("-"*60)
        print("Salário líquido:", employee.calculateSalary())
        print("-"*60)
    elif opt == "0":
        print("-"*60)
        main()
    else:
        print("-"*60)
        ErrorMessage("Opção inválida")


# Administrator Functions
def adminMenu():
    while True:
        print("1. Registrar administrador")
        print("2. Ver informações do administrador")
        print("3. Ver salário líquido")
        print("0. Voltar")
        option = input("Opção: ")
        return option

def getAdminInfos():
    subsistenceAllowance = floatVerify("Auxílio de custos: ")
    if subsistenceAllowance > 0:
        return subsistenceAllowance
    else:
        ErrorMessage("Valor inválido")
        return getAdminInfos()

def adminActions(opt):
    global administrator

    if opt == "1":
        name, cpf, rg, phone = userRegister()
        sectorCode, baseSalary, tax = getEmployeeInfos()
        subsistenceAllowance = getAdminInfos()
        administrator = Administrator(name, cpf, rg, phone, sectorCode, baseSalary, tax, subsistenceAllowance)
    elif opt == "2":
        print("-"*60)
        administrator.showInfos()
        print("-"*60)
    elif opt == "3":
        print("-"*60)
        print("Salário líquido:", administrator.calculateSalary())
        print("-"*60)
    elif opt == "0":
        print("-"*60)
        main()
    else:
        print("-"*60)
        ErrorMessage("Opção inválida")

#Factory Worker
def factWorkerMenu():
    while True:
        print("1. Registrar trabalhador")
        print("2. Ver informações do trabalhador")
        print("3. Ver salário líquido")
        print("0. Voltar")
        option = input("Opção: ")
        return option
    
def getFactWorkerInfos():
    valueProduction = floatVerify("Valor da produção: ")
    commission = floatVerify("Comissão (em porcentagem): ")
    if valueProduction > 0 and 0 < commission < 100:
        return valueProduction, commission
    else:
        ErrorMessage("Valores inválidos")
        return getFactWorkerInfos()
    
def factWorkerActions(opt):
    global factWorker

    if opt == "1":
        name, cpf, rg, phone = userRegister()
        sectorCode, baseSalary, tax = getEmployeeInfos()
        valueProduction, commission = getFactWorkerInfos()
        factWorker = FactoryWorker(name, cpf, rg, phone, sectorCode, baseSalary, tax, valueProduction, commission)
    elif opt == "2":
        print("-"*60)
        factWorker.showInfos()
        print("-"*60)
    elif opt == "3":
        print("-"*60)
        print("Salário líquido:", factWorker.calculateSalary())
        print("-"*60)
    elif opt == "0":
        print("-"*60)
        main()
    else:
        print("-"*60)
        ErrorMessage("Opção inválida")

# General Functions
def userTypeMenu():

    print("1. Usuário comum")
    print("2. Fornecedor")
    print("3. Empregado")
    print("4. Administrador")
    print("5. Trabalhador de fábrica")
    print("0. Sair do programa")

    userType = input("Opção: ")
    return userType

def main():
    userType = userTypeMenu()
    while True:
        if userType == "1":
            #Usuário comum
            option = comumUserMenu()
            userActions(option)
        elif userType == "2":
            #Fornecedor
            option = supplierMenu()
            supplierActions(option)
        elif userType == "3":
            #Empregado
            option = employeeMenu()
            employeeActions(option)
        elif userType == "4":
            #Administrador
            option = adminMenu()
            adminActions(option)
        elif userType == "5":
            #Factory worker
            option = factWorkerMenu()
            factWorkerActions(option)
        elif userType == "0":
            print("-"*60)
            print("Fechando programa")
            break
        else:
            ErrorMessage("Opção inválida")

main()