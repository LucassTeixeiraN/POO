class Bank:
    def __init__(self):
        self.accounts = []
    
    def find_account(self, name, pin):
        for account in self.accounts:
            if account.name == name and account.pin == pin:
                return account
        return None

    def list_accounts(self):
        for account in self.accounts:
            print(account)

    def delete_account(self, name, pin):
        account = self.find_account(name, pin)
        if account:
            self.accounts.remove(account)
            print("Conta deletada com sucesso!")
        else:
            print("Conta não encontrada.")

    def update_pin(self, name, old_pin, new_pin):
        account = self.find_account(name, old_pin)
        if account:
            account.pin = new_pin
            print("PIN atualizado com sucesso!")
        else:
            print("Conta não encontrada.")

    def transfer(self, from_name, from_pin, to_name, to_pin, amount):
        from_account = self.find_account(from_name, from_pin)
        to_account = self.find_account(to_name, to_pin)
        if from_account and to_account:
            if from_account.withdraw(amount) is None:
                to_account.deposit(amount)
                print("Transferência realizada com sucesso!")
            else:
                print("Transferência não realizada. Verifique o saldo da conta de origem.")
        else:
            print("Conta não encontrada.")

    def add_account(self, account):
        self.accounts.append(account)
        print("Conta criada com sucesso!")

    def deposit(self, name, pin, amount):
        account = self.find_account(name, pin)
        if account:
            account.deposit(amount)
            print("Depósito realizado com sucesso!")
        else:
            print("Conta não encontrada.")

    def withdraw(self, name, pin, amount):
        account = self.find_account(name, pin)
        if account:
            result = account.withdraw(amount)
            if result is None:
                print("Saque realizado com sucesso!")
            else:
                print(result)
        else:
            print("Conta não encontrada.")

    def get_balance(self, name, pin):
        account = self.find_account(name, pin)
        if account:
            print("Saldo:", account.get_balance())
        else:
            print("Conta não encontrada.")

    def get_account_info(self, name, pin):
        account = self.find_account(name, pin)
        if account:
            print(account)
        else:
            print("Conta não encontrada.")

    def compute_interest(self, name, pin):
        account = self.find_account(name, pin)
        if account:
            interest = account.compute_interest()
            print("Juros:", interest)
        else:
            print("Conta não encontrada.")