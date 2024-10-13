'''Implemente a classe Bank considerando os métodos listados abaixo e acrescentando
métodos que considerar conveniente.'''

class SavingsAccount:
    RATE = 0.02

    def __init__(self, name, pin, balance=0.0):
        self.name = name
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return None

    def withdraw(self, amount):
        if amount < 0:
            return "Amount must be >= 0"
        elif self.balance < amount:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return None

    def computeInterest(self):
        interest = self.balance * SavingsAccount.RATE
        self.deposit(interest)
        return interest

    def __str__(self):
        result = 'Name:' + self.name + '\n'
        result += 'PIN:' + str(self.pin) + '\n'
        result += 'Balance:' + str(self.balance)
        return result


class BankAccountManager:  # Nova classe para somente gerenciar as contas do banco(adicionar, encontrar, depositar, etc)
    def __init__(self, bank):
        self.bank = bank

    def addAccount(self, name, pin, balance=0):
        account = SavingsAccount(name, pin, balance)
        self.bank.accounts.append(account)
        print("Conta criada com sucesso!")

    def findAccount(self, name, pin):
        for account in self.bank.accounts:
            if account.name == name and account.pin == pin:
                return account
        return None

    def deposit(self, name, pin, amount):
        account = self.findAccount(name, pin)
        if account:
            account.deposit(amount)
            print("Depósito realizado com sucesso!")
        else:
            print("Conta não encontrada.")

    def withdraw(self, name, pin, amount):
        account = self.findAccount(name, pin)
        if account:
            result = account.withdraw(amount)
            if result is None:
                print("Saque realizado com sucesso!")
            else:
                print(result)
        else:
            print("Conta não encontrada.")

    def getBalance(self, name, pin):
        account = self.findAccount(name, pin)
        if account:
            print("Saldo:", account.balance)
        else:
            print("Conta não encontrada.")

    def getAccountInfo(self, name, pin):
        account = self.findAccount(name, pin)
        if account:
            print(account)
        else:
            print("Conta não encontrada.")

    def computeInterest(self, name, pin):
        account = self.findAccount(name, pin)
        if account:
            interest = account.computeInterest()
            print("Juros:", interest)
        else:
            print("Conta não encontrada.")


class Bank:
    def __init__(self):
        self.accounts = []
        self.account_manager = BankAccountManager(self)

    def listAccounts(self):
        if len(self.accounts) > 0:
            for account in self.accounts:
                print(account)
        else:
            print("No accounts registered.")

    def deleteAccount(self, name, pin):
        account = self.account_manager.findAccount(name, pin)
        if account:
            self.accounts.remove(account)
            print("Conta deletada com sucesso!")
        else:
            print("Conta não encontrada.")

    def updatePin(self, name, old_pin, new_pin):
        account = self.account_manager.findAccount(name, old_pin)
        if account:
            account.pin = new_pin
            print("PIN atualizado com sucesso!")
        else:
            print("Conta não encontrada.")

    def transfer(self, from_name, from_pin, to_name, to_pin, amount):
        from_account = self.account_manager.findAccount(from_name, from_pin)
        to_account = self.account_manager.findAccount(to_name, to_pin)
        if from_account and to_account:
            if from_account.withdraw(amount) is None:
                to_account.deposit(amount)
                print("Transferência realizada com sucesso!")
            else:
                print("Transferência não realizada. Verifique o saldo da conta de origem.")
        else:
            print("Conta não encontrada.")


def menu():
    print("Opções:")
    print("1. Criar conta")
    print("2. Depositar dinheiro")
    print("3. Sacar dinheiro")
    print("4. Consultar saldo")
    print("5. Obter informações da conta")
    print("6. Calcular juros")
    print("7. Deletar conta")
    print("8. Atualizar PIN")
    print("9. Transferir dinheiro")
    print("10. Listar contas")
    print("11. Sair")

    option = int(input("Escolha uma opção: "))
    if option < 1 or option > 11:
        print("Erro: Opcao invalida.")
    return option


def main():
    bank = Bank()
    while True:
        try:
            if input("Aperte ENTER para ir ao MENU. ") == '':
                option = menu()
                if option == 1:
                    name = input("Digite o nome: ")
                    pin = int(input("Digite o PIN: "))
                    balance = float(input("Digite o saldo inicial (opcional): ") or 0)
                    if any(account.pin == pin for account in bank.accounts):
                        print("Erro: PIN já existe.")
                    else:
                        bank.account_manager.addAccount(name, pin, balance)
                elif option == 2:
                    name = input("Digite o nome: ")
                    pin = int(input("Digite o PIN: "))
                    amount = float(input("Digite o valor do depósito: "))
                    bank.account_manager.deposit(name, pin, amount)
                elif option == 3:
                    name = input("Digite o nome: ")
                    pin = int(input("Digite o PIN: "))
                    amount = float(input("Digite o valor do saque: "))
                    bank.account_manager.withdraw(name, pin, amount)
                elif option == 4:
                    name = input("Digite o nome: ")
                    pin = int(input("Digite o PIN: "))
                    bank.account_manager.getBalance(name, pin)
                elif option == 5:
                    name = input("Digite o nome: ")
                    pin = int(input("Digite o PIN: "))
                    bank.account_manager.getAccountInfo(name, pin)
                elif option == 6:
                    name = input("Digite o nome: ")
                    pin = int(input("Digite o PIN: "))
                    bank.account_manager.computeInterest(name, pin)
                elif option == 7:
                    name = input("Digite o nome: ")
                    pin = int(input("Digite o PIN: "))
                    bank.deleteAccount(name, pin)
                elif option == 8:
                    name = input("Digite o nome: ")
                    old_pin = int(input("Digite o PIN antigo: "))
                    new_pin = int(input("Digite o PIN novo: "))
                    bank.updatePin(name, old_pin, new_pin)
                elif option == 9:
                    from_name = input("Digite o nome da conta de origem: ")
                    from_pin = int(input("Digite o PIN da conta de origem: "))
                    to_name = input("Digite o nome da conta de destino: ")
                    to_pin = int(input("Digite o PIN da conta de destino: "))
                    amount = float(input("Digite o valor da transferência: "))
                    bank.transfer(from_name, from_pin, to_name, to_pin, amount)
                elif option == 10:
                    bank.listAccounts()
                elif option == 11:
                    print("Saindo...")
                    break
        except ValueError:
            print("Erro: Valor inválido.")
main()