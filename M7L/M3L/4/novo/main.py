from person import Person
from account import Account
from bank import Bank

bank: Bank = None

def floatVerify(msg):
    try:
        number = float(input(msg))
        return number
    except ValueError:
        errorMessage()
        return floatVerify(msg)
    
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

def errorMessage():
    print("Valor inválido")

def createAccount():
    while True:
        client = createClient()
        accountNumber = input("Número da conta: ")
        balance = floatVerify("Saldo: ")
        return Account(client, accountNumber, balance)
            
def searchAccount():
    global bank
    
    search = input("Insira o nome ou o documento do titular: ")
    searchName = bank.clientByName(search)
    searchDocument = bank.clientByDocument(search)
    if searchName:
        bank.accountInfos(searchName)
    elif searchDocument:
        bank.accountInfos(searchDocument)
    else:
        print("Essa conta não existe")

def debitAccount():
    account = searchAccount()
    if account:
        amount = floatVerify("Digite quanto você deseja retirar da conta: ")
        bank.decreaseBalance(account, amount)
        
def depositAccount():
    account = searchAccount()
    if account:
        amount = floatVerify("Digite quanto você deseja depositar na conta: ")
        bank.increaseBalance(account, amount)

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

        elif option == "5":
            print("Saindo do programa")
            break
        else:
            print("Opção inválida")            
main()