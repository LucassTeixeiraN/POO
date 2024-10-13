'''3. Crie uma classe chamada VendingMachine que simule uma máquina de venda de
produtos. Essa classe deve permitir cadastrar produtos, selecionar um produto para
compra, inserir dinheiro, retornar o troco e exibir o estoque disponível.'''

from product import Product
from slot import Slot

class VendingMachine:

    def __init__(self):
        self.__slots = []

    def getSlots(self):
        return self.__slots

    def addSlot(self, slot: Slot):
        self.__slots.append(slot)
    
    @staticmethod
    def findSlot(slot, slotNumber):
        if slot.getSlotNumber() == slotNumber:
            return True
        return False
    
    @staticmethod
    def quantityVerify(slot):
        if slot.getQuantity() > 0:
            return True
        return False
    
    @staticmethod
    def changeVerify(change):
        if change > 0:
            return True
        return False
    
    @staticmethod
    def errorMessage(err):
        print(err)

    def sellProduct(self, slotNumber, money):
        slot = self.getSlotByNumber(slotNumber)
        if slot is None:
            self.errorMessage("Slot inválido!")
            return

        if not self.isProductAvailable(slot):
            self.errorMessage("Produto esgotado!")
            return

        change = self.calculateChange(money, slot.getProduct().getPrice())
        if not self.changeVerify(change):
            self.errorMessage("Dinheiro insuficiente!")
            return

        self.completeSale(slot, change)

    def getSlotByNumber(self, slotNumber):
        for slot in self.__slots:
            if self.findSlot(slot, slotNumber):
                return slot
        return None

    @staticmethod
    def isProductAvailable(slot):
        return slot.getQuantity() > 0

    @staticmethod
    def calculateChange(money, price):
        return money - price

    @staticmethod
    def completeSale(slot, change):
        slot.decreaseQuantity()
        print("-" * 60)
        print("Produto vendido!")
        print(f"Troco: ${change:.2f}")


    def showProducts(self):
        print("-"*60)
        for slot in self.__slots:
            product = slot.getProduct()
            print(f"Slot {slot.getSlotNumber() + 1}: {product.getName()} - ${product.getPrice():.2f} ({slot.getQuantity()} disponíveis)")