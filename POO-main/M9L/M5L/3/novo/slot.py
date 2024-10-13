from product import Product

class Slot:
    def __init__(self, slotNumber, product: Product, quantity):
        self.__slotNumber = slotNumber
        self.__product = product
        self.__quantity = quantity
        self.__product.setSlot(self)  

    def getSlotNumber(self):
        return self.__slotNumber
    
    def getProduct(self):
        return self.__product
    
    def getQuantity(self):
        return self.__quantity
    
    def decreaseQuantity(self):
        if self.__quantity > 0:
            self.__quantity -= 1