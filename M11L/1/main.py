'''Crie uma classe Person, contendo os atributos encapsulados, com seus respectivos
seletores (getters) e modificadores (setters), e ainda o construtor padrão. Atributos:
nome, endereço, CPF, RG e telefone.'''

from comunUser import ComunUser

user: ComunUser = None

def ErrorMessage(err):
    print(err)

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
        userType = "Usuário comum"
        name, cpf, rg, phone = userRegister()
        user = ComunUser(name, cpf, rg, phone, userType)
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

# General Functions
def userTypeMenu():

    print("1. Usuário comum")
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
        elif userType == "0":
            print("-"*60)
            print("Fechando programa")
            break
        else:
            ErrorMessage("Opção inválida")

main()