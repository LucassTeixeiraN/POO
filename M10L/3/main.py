'''Considere, como subclasse da classe Person, a classe Employee. Considere que
cada instância da classe Employee tem, para além dos atributos que caracterizam a
classe Person, os atributos sectorCode (inteiro), baseSalary (vencimento base) e tax
(porcentagem retida dos impostos). Implemente a classe Employee com métodos
seletores e modificadores e um método calculateSalary. Altere o main para que você
possa verificar o funcionamento dos métodos implementados na classe Employee e
os herdados da classe Person.'''

from person import Person
from supplier import Supplier
from employee import Employee

user: Person = None
supplier: Supplier = None
employee: Employee = None

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
    return credit, debit


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
    return sectorCode, baseSalary, tax

def employeeAction(opt):
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
        userTypeMenu()
    else:
        print("-"*60)
        ErrorMessage("Opção inválida")

# General Functions
def userTypeMenu():

    print("1. Usuário comum")
    print("2. Fornecedor")
    print("3. Empregado")
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
            supplierActions(option)
        elif userType == "0":
            print("-"*60)
            print("Fechando programa")
            break
        else:
            ErrorMessage("Opção inválida")

main()