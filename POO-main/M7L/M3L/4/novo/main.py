from person import Person
from account import Account
from bank import Bank

def menu():
    print("\nMenu:")
    print("1. Criar conta")
    print("2. Retirar dinheiro da conta")
    print("3. Depositar dinheiro na conta")
    print("4. Verificar saldo da conta")
    print("5. Sair")

    option = input("Escolha uma opção: ")
    return option

def createClient():
    name = input("Nome do titular: ")
    documento = input("Documento do titular: ")
    client = Person(name, documento)
    return client

def verifyFloat(number):
    try:
        float(number)
        return True
    except ValueError:
        return False

def errorMessage():
    print("Valor inválido")

def createAccount():
    while True:
        client = createClient()
        accountNumber = input("Número da conta: ")
        balance = input("Saldo: ")
        if verifyFloat(balance):
            account = Account(client, accountNumber, float(balance))
            return account
        else:
            errorMessage()
            
def searchAccount():
    search = input("Insira o nome ou o documento do titular: ")
    searchName = bank.clientByName(search)
    searchDocument = bank.clientByDocument(search)
    if searchName:
        return searchName
    elif searchDocument:
        return searchDocument
    else:
        print("Essa conta não existe")
        return False

def debitAccount():
    account = searchAccount()
    if account:
        amount = input("Digite quanto você deseja retirar da conta: ")
        if verifyFloat(amount):
            bank.decreaseBalance(account, float(amount))
        else:
            errorMessage()
            debitAccount()
        
def depositAccount():
    account = searchAccount()
    if account:
        amount = input("Digite quanto você deseja depositar na conta: ")
        if verifyFloat(amount):
            bank.increaseBalance(account, float(amount))
        else:
            errorMessage()
            depositAccount()

def main():
    global bank
    bank = Bank()
    while True:
        option = menu()
        if option == "1":
            newAccount = createAccount()
            bank.addAccount(newAccount)
        elif option == "2":
            debitAccount()
        elif option == "3":
            depositAccount()
        elif option == "4":
            account = searchAccount()
            bank.accountInfos(account)
        elif option == "5":
            print("Saindo do programa")
            break
        else:
            print("Opção inválida")            
main()