from bank import Bank
class Menu:
    def __init__(self):
        self.bank = Bank()

    def show_menu(self):
        print("Opções:")
        print("1. Criar conta")
        print("2. Depositar dinheiro")
        print("3. Sacar dinheiro")
        print("4. Consultar saldo")
        print("5. Obter informações da conta")
        print("6. Calcular juros")
        print("7. Sair")

    def get_option(self):
        option = int(input("Escolha uma opção: "))
        if option < 1 or option > 7:
            print("Erro: Opcao invalida.")
        return option
