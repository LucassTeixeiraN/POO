from menu import Menu
from bank import Bank
from account import Account
from savingsAccount import SavingsAccount

def main():
    menu = Menu()
    bank = Bank()
    while True:
        if input("Aperte ENTER para ir ao MENU. ") == '':
            try:
                menu.show_menu()
                option = menu.get_option()
                if option == 1:
                    name = input("Digite o nome: ")
                    pin = int(input("Digite o PIN: "))
                    balance = float(input("Digite o saldo inicial (opcional): ") or 0)
                    account = SavingsAccount(name, pin, balance)
                    bank.add_account(account)
                elif option == 2:
                    name = input("Digite o nome: ")
                    pin = int(input("Digite o PIN: "))
                    amount = float(input("Digite o valor do depósito: "))
                    bank.deposit(name, pin, amount)
                elif option == 3:
                    name = input("Digite o nome: ")
                    pin = int(input("Digite o PIN: "))
                    amount = float(input("Digite o valor do saque: "))
                    bank.withdraw(name, pin, amount)
                elif option == 4:
                    name = input("Digite o nome: ")
                    pin = int(input("Digite o PIN: "))
                    bank.get_balance(name, pin)
                elif option == 5:
                    name = input("Digite o nome: ")
                    pin = int(input("Digite o PIN: "))
                    bank.get_account_info(name, pin)
                elif option == 6:
                    name = input("Digite o nome: ")
                    pin = int(input("Digite o PIN: "))
                    bank.compute_interest(name, pin)
                elif option == 7:
                    print("Saindo...")
                    break
                else:
                    print("Invalid option.")
            except(ValueError):
                print("Error: Invalid option.")            
main()