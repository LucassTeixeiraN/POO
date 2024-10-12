'''3. Crie uma classe chamada VendingMachine que simule uma máquina de venda de
produtos. Essa classe deve permitir cadastrar produtos, selecionar um produto para
compra, inserir dinheiro, retornar o troco e exibir o estoque disponível.'''

from vendingMachine import VendingMachine

def menu():
    try:
        print("-"*60)
        option = int(input("Escolha uma opção:\n1- Registrar produtos\n2- Visualizar produtos\n3- Comprar um produto\n4- Sair\n"))
        return option
    except ValueError:
        errorMessage()
        menu()

def errorMessage():
    print("-"*60)
    print("Insira uma opção válida")

def main():
    vendingMachine = VendingMachine()
    while True:
        try:
            option = menu()
            if option == 1:
                print("-"*60)
                name = input("Insira o nome do produto: ")
                price = float(input("Insira o preço do produto: "))
                amount = int(input("Insira a quantidade do produto: "))
                vendingMachine.registerProduct(name, price, amount)
            elif option == 2:
                vendingMachine.showProducts()
            elif option == 3:
                print("-"*60)
                product = int(input("Insira o número do produto que deseja comprar: "))
                money = float(input("Insira quanto você irá pagar pelo produto: "))
                vendingMachine.buyProduct(product-1, money)
            elif option == 4:
                print("-"*60)
                print("Saindo do programa")
                print("-"*60)
                break
            else:
                errorMessage()
        except ValueError:
            errorMessage()

main()

