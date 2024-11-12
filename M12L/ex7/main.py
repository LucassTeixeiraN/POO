'''Crie uma classe Account com um método chamado update() que atualiza a conta de
acordo com a taxa percentual:
class Account:
    def update(self, tax):
        self._balance += self._balance * tax
Crie duas subclasses da classe Account: CurrentAccount e SavingsAccount. Ambas
terão o método update() reescrito: a CurrentAccount deve atualizar-se com o dobro
da taxa e a SavingsAccount deve atualizar-se com o triplo da taxa.'''
from account import Account, CurrentAccount, SavingsAccount

def menu():
    print("\n--- Menu Bancário ---")
    print("1. Criar conta")
    print("2. Criar conta corrente")
    print("3. Criar conta poupança")
    print("4. Atualizar saldo")
    print("5. Ver saldo")
    print("6. Sair")
    return input("Escolha uma opção (1-6): ")

def main():
    account = None
    
    while True:        
        option = menu()

        if option == '1':
            balance = float(input("Digite o saldo inicial da conta: R$"))
            account = Account(balance)
            print("Conta criada com sucesso!")

        elif option == '2':
            balance = float(input("Digite o saldo inicial da conta corrente: R$"))
            account = CurrentAccount(balance)
            print("Conta corrente criada com sucesso!")

        elif option == '3':
            balance = float(input("Digite o saldo inicial da conta poupança: R$"))
            account = SavingsAccount(balance)
            print("Conta poupança criada com sucesso!")

        elif option == '4':
            if account is not None:
                tax = float(input("Digite a taxa de atualização (ex: 0.05 para 5%): "))
                account.update(tax)
                print("Saldo atualizado com sucesso!")
            else:
                print("Nenhuma conta criada. Crie uma conta antes de ver o saldo.")

        elif option == '5':
            if account is not None:
                print(f"Saldo atual: R${account.getBalance():.2f}")
            else:
                print("Nenhuma conta criada. Crie uma conta antes de ver o saldo.")

        elif option == '6':
            print("Saindo...")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()