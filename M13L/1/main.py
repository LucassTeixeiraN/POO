'''1. Implemente um sistema de Banco com seus 3 tipos de contas (corrente, poupança e
investimento), evidenciando a classe Account como uma classe abstrata.'''

from checkingAccount import CheckingAccount
from savingAccount import SavingAccount
from investmentAccount import InvestimentAccount
from bank import Bank

def menu():
    print("1. Criar conta")
    print("2. Verificar conta")
    print("3. Depositar dinheiro")
    print("4. Transferir dinheiro")
    print("5. Calcular rendimento da conta")
    print("6. Investir")

    return input("Escolha uma opção: ")

def verifyFloat(msg):
    try:
        number = float(input(msg))
        return number
    except:
        print("Valor inválido")
        return verifyFloat(msg)

def verifyInt(msg):
    try:
        number = int(input(msg))
        return number
    except:
        print("Valor inválido")
        return verifyInt(msg)

def colectUserInfos():
    name = input("Nome: ")
    document = input("Documento: ")
    accountNumber = input("Número da conta: ")
    balance = verifyFloat("Saldo da conta: ")
    if not bank.findAccount(accountNumber) and not bank.findAccountByDocument(document):
        return name, document, accountNumber, balance
    else:
        print("O documento e/ou o número da conta já está sendo usado")
        print("-"*60)
        return colectUserInfos()

def newCheckingAccount():
    name, document, accountNumber, balance = colectUserInfos()
    return CheckingAccount(name, document, accountNumber, balance, "corrente")

def newSavingAccount():
    name, document, accountNumber, balance = colectUserInfos()
    tax = verifyFloat("Taxa aplicada ao mês (em porcentagem): ")
    return SavingAccount(name, document, accountNumber, balance, "poupança", tax/100)

def newInvestmentAccount():
    name, document, accountNumber, balance = colectUserInfos()
    return InvestimentAccount(name, document, accountNumber, balance, "investimento")

def createAccountMenu():
    print("-"*60)
    print("1. Conta corrente")
    print("2. Conta poupança")
    print("3. Conta de investimentos")
    print("0. Voltar")
    return input("Escolha um tipo de conta: ")

def createAccount():
    accountType = createAccountMenu()
    if accountType == "1":
        return newCheckingAccount()
    elif accountType == "2":
        return newSavingAccount()
    elif accountType == "3":
        return newInvestmentAccount()

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
            if account:
                value = verifyFloat("Valor a ser depositado: ")
                account.deposit(value)
            else:
                print("Essa conta não existe")
        elif option == "4":
            account = checkAccount()
            if account and account.getAccountType() == "corrente":
                value = verifyFloat("Valor a ser transferido: ")
                account.transfer(value)
            else:
                print("Essa conta não existe ou não é uma conta corrente")
        elif option == "5":
            account = checkAccount()
            if account and account.getAccountType() == "poupança":
                time = verifyInt("Insira o tempo em meses: ")
                gain = account.calculateGain(time)
                if time > 0:
                    print(f"Ganho estimado: R${gain:.2f}")
                else:
                    print("Valor inválido")
            else:
                print("Essa conta não existe ou não é uma poupança")

        elif option == "6":
            account = checkAccount()
            if account and account.getAccountType() == "investimento":
                account.calculateInvestment()
            else:
                print("Essa conta não existe ou não é uma conta de investimento")
main()