'''3. Crie uma classe chamada VendingMachine que simule uma máquina de venda de
produtos. Essa classe deve permitir cadastrar produtos, selecionar um produto para
compra, inserir dinheiro, retornar o troco e exibir o estoque disponível.'''

from vendingMachine import VendingMachine
from product import Product


def errorMessage():
    print("-"*60)
    print("Valor inválido")

def floatVerify(msg):
    try:
        number = float(input(msg))
        return number
    except ValueError:
        errorMessage()
        return floatVerify()

def intVerify(msg):
    try:
        number = int(input(msg))
        return number
    except ValueError:
        errorMessage()
        return intVerify()

def menu():
    print("-"*60)
    option = input("Escolha uma opção:\n1- Registrar produtos\n2- Visualizar produtos\n3- Comprar um produto\n4- Sair\n")
    return option


def moneyVerify(money):
    return money > 0

def amountVerify(amount):
    return amount > 0

def newProduct():
    print("-"*60)
    name = input("Insira o nome do produto: ")
    price = floatVerify("Insira o preço do produto: ")
    amount = intVerify("Insira a quantidade do produto: ")
    if moneyVerify(price) and amountVerify(amount):
        product = Product(name, price, amount)
        return product
    else:
        errorMessage()
        newProduct()

def buyItem():
    print("-"*60)
    product = intVerify("Insira o número do produto que deseja comprar: ")
    money = floatVerify("Insira quanto você irá pagar pelo produto: ")
    if moneyVerify(money):
        return (product - 1, money)
    else:
        errorMessage()
        buyItem()

def main():
    vendingMachine = VendingMachine()

    while True:
        try:
            option = menu()
            if option == '1':
                vendingMachine.registerProduct(newProduct())
            elif option == '2':
                vendingMachine.showProducts()
            elif option == '3':
                item = buyItem()
                vendingMachine.buyProduct(item[0], item[1])
            elif option == '4':
                print("-"*60)
                print("Saindo do programa")
                print("-"*60)
                break
            else:
                errorMessage()
        except ValueError:
            errorMessage()

main()
