
class Product:
    def __init__(self, code: int, value: float, description: str) -> None:
        self.__code = code
        self.__value = value
        self.__description = description

    def getValue(self):
        return self.__value


class ItemOrder:
    def __init__(self, product:Product, quantity) -> None:
        self.__product = product
        self.__quantity = quantity

    def getProduct(self):
        return self.__product
    
    def getQuantity(self):
        return self.__quantity


class Order:
    def __init__(self) -> None:
        self.__total = 0
        self.__orders = []
    
    def getTotal(self) -> float:
        for item in self.__orders:
            self.__total += item.getProduct().getValue() * item.getQuantity()

        return self.__total

    def addItem(self, item: ItemOrder) -> None:
        self.__orders.append(item)



def main():
    cellphone = Product(1, 3000, "Celular")
    computer = Product(2, 5000, "Computador")
    mouse = Product(3, 150, "Mouse")

    myBuy = Order()

    myBuy.addItem(ItemOrder(cellphone, 2))
    myBuy.addItem(ItemOrder(computer, 1))
    myBuy.addItem(ItemOrder(mouse, 4))

    print(f"Total da compra: R${myBuy.getTotal():.2f}")

main()


    
