'''1. Implemente um sistema de Banco com seus 3 tipos de contas (corrente, poupança e
investimento), evidenciando a classe Account como uma classe abstrata.'''

from checkingAccount import CheckingAccount
from savingAccount import SavingAccount
from bank import Bank

def menu():
    print("1. Criar conta")
    print("2. Verificar conta")
    print("3. Depositar dinheiro")
    print("4. Transferir dinheiro")

    return input("Escolha uma opção: ")

def verifyFloat(msg):
    try:
        number = float(input(msg))
        return number
    except:
        print("Valor inválido")
        return verifyFloat(msg)

def colectUserInfos():
    name = input("Nome: ")
    document = input("Documento: ")
    accountNumber = input("Número da conta: ")
    balance = verifyFloat("Saldo da conta: ")
    return name, document, accountNumber, balance

def newCheckingAccount():
    name, document, accountNumber, balance = colectUserInfos()
    return CheckingAccount(name, document, accountNumber, balance, "checking")

def createAccount():
    print("-"*60)
    print("1. Conta corrente")
    print("2. Conta poupança")
    print("3. Conta de investimentos")
    print("3. Voltar")
    accountType = input("Escolha um tipo de conta: ")
    if accountType == "1":
        return newCheckingAccount()

def checkAccount():
    numberAccount = input("Número da conta: ")
    account = bank.findAccount(numberAccount)
    return account



def main():
    global bank
    bank = Bank()

    while True:
        option = menu()

        if option == "1":
            bank.addAccount(createAccount())
        elif option == "2":
            account = checkAccount()
            if account:
                account.showAccount()
            else:
                print("Essa conta não existe")
        elif option == "3":
            account = checkAccount()
            if account and account.getAccountType == "checking":
                value = verifyFloat("Valor a ser depositado: ")
                account.deposit(value)
            else:
                print("Essa conta não existe ou não é uma conta corrente")
        elif option == "4":
            account = checkAccount()
            if account and account.getAccountType == "checking":
                value = verifyFloat("Valor a ser transferido: ")
                account.transfer(value)
            else:
                print("Essa conta não existe ou não é uma conta corrente")

main()