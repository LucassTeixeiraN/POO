'''3. Crie uma classe chamada VendingMachine que simule uma máquina de venda de
produtos. Essa classe deve permitir cadastrar produtos, selecionar um produto para
compra, inserir dinheiro, retornar o troco e exibir o estoque disponível.'''

class VendingMachine:
    __nameList = ["Coca-cola", "Água"]
    __priceList = [8.50, 3.30]
    __amountList = [5, 10]

    @classmethod
    def registerProduct(cls, product: any):
        cls.__nameList.append(product.getName())
        cls.__priceList.append(product.getPrice())
        cls.__amountList.append(product.getAmount())
    
    @classmethod
    def buyProduct(cls, product, money):
        if cls.__storageCheck(cls.__amountList[product]):
            print("Esgotado")
        elif cls.__moneyCheck(money, cls.__priceList[product]):
            print("Dinheiro insuficiente")
        else:
            print(f"Troco devido R${cls.__changeCalculate(money, cls.__priceList[product]):.2f}")
            cls.__amountDecreasement(product)

    @staticmethod
    def __storageCheck(product):
        if  product < 0:
            return True
        return False
    
    @staticmethod
    def __moneyCheck(money, price):
        if money < price:
            return True
        return False
    
    @staticmethod
    def __changeCalculate(money, price):
        return money-price
    
    @classmethod
    def __amountDecreasement(cls, product):
        cls.__amountList[product] -= 1

    @classmethod
    def showProducts(cls):
        print("-"*60)
        for i in range(len(cls.__nameList)):
            print(f"{i+1}- {cls.__nameList[i]} R${cls.__priceList[i]:.2f} ({cls.__amountList[i]} unidades)")