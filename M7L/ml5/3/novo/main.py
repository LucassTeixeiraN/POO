'''3. Crie uma classe chamada VendingMachine que simule uma máquina de venda de
produtos. Essa classe deve permitir cadastrar produtos, selecionar um produto para
compra, inserir dinheiro, retornar o troco e exibir o estoque disponível.'''

from vendingMachine import VendingMachine
from product import Product

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
    print("Valor inválido")

def newProduct():
    try:
        print("-"*60)
        name = input("Insira o nome do produto: ")
        price = float(input("Insira o preço do produto: "))
        amount = int(input("Insira a quantidade do produto: "))
        product = Product(name, price, amount)
        return product

    except ValueError:
        errorMessage()
        newProduct()

def buyItem():
    try:
        print("-"*60)
        product = int(input("Insira o número do produto que deseja comprar: "))
        money = float(input("Insira quanto você irá pagar pelo produto: "))
        return (product - 1, money)
    except ValueError:
        errorMessage()
        buyItem()

def main():
    vendingMachine = VendingMachine()

    while True:
        try:
            option = menu()
            if option == 1:
                vendingMachine.registerProduct(newProduct())
            elif option == 2:
                vendingMachine.showProducts()
            elif option == 3:
                item = buyItem()
                vendingMachine.buyProduct(item[0], item[1])
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

