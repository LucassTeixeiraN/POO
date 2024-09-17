'''3. Crie uma classe chamada VendingMachine que simule uma máquina de venda de
produtos. Essa classe deve permitir cadastrar produtos, selecionar um produto para
compra, inserir dinheiro, retornar o troco e exibir o estoque disponível.'''

class VendingMachine:
    __nameList = ["Coca-cola", "Água"]
    __priceList = [8.50, 3.30]
    __amountList = [5, 10]

    @classmethod
    def registerProduct(cls, name, price, amount):
        cls.__nameList.append(name)
        cls.__priceList.append(price)
        cls.__amountList.append(amount)
    
    @classmethod
    def buyProduct(cls, product, money):
        if cls.__storageCheck(product):
            print("Esgotado")
        elif cls.__moneyCheck(money, product):
            print("Dinheiro insuficiente")
        else:
            print(f"Troco devido R${cls.__changeCalculate(money, product):.2f}")
            cls.__amountDecreasement(product)

    @classmethod
    def __storageCheck(cls, product):
        if cls.__amountList[product] < 0:
            return True
        return False
    
    @classmethod
    def __moneyCheck(cls, money, product):
        if money < cls.__priceList[product]:
            return True
        return False
    
    @classmethod
    def __changeCalculate(cls, money, product):
        return money-cls.__priceList[product]
    
    @classmethod
    def __amountDecreasement(cls, product):
        cls.__amountList[product] -= 1

    @classmethod
    def showProducts(cls):
        print("-"*60)
        for i in range(len(cls.__nameList)):
            print(f"{i+1}- {cls.__nameList[i]} R${cls.__priceList[i]:.2f} ({cls.__amountList[i]} unidades)")
