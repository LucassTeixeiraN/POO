'''3. Crie uma classe chamada VendingMachine que simule uma máquina de venda de
produtos. Essa classe deve permitir cadastrar produtos, selecionar um produto para
compra, inserir dinheiro, retornar o troco e exibir o estoque disponível.'''

from vendingMachine import VendingMachine
from product import Product
from slot import Slot



def menu():
    try:
        print("-"*60)
        option = int(input("Escolha uma opção:\n1- Registrar produtos\n2- Visualizar produtos\n3- Comprar um produto\n4- Sair\n"))
        return option
    except ValueError:
        errorMessage()
        menu()

def intVerify(num):
    try:
        number = int(num)
        return number
    except ValueError:
        errorMessage()
        return -1

def errorMessage():
    print("-"*60)
    print("Valor inválido")


def newProduct():
    try:
        print("-"*60)
        name = input("Insira o nome do produto: ")
        price = float(input("Insira o preço do produto: "))
        product = Product(name, price)
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

def createSlot():
    global slotAmount
    product = newProduct()
    amount = input(f"Insira a quantidade do produto {product.getName()}: ")
    if intVerify(amount) != -1:
        slot = Slot(slotAmount, product, int(amount))
        slotAmount += 1
        return slot
    else:
        createSlot()


def main():
    global vendingMachine, slotAmount
    vendingMachine = VendingMachine()
    slotAmount = 0
    
    while True:
        try:
            option = menu()
            if option == 1:
                vendingMachine.addSlot(createSlot())
            elif option == 2:
                vendingMachine.showProducts()
            elif option == 3:
                item = buyItem()
                vendingMachine.sellProduct(item[0], item[1])
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

