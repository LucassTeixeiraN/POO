'''Crie uma classe chamada VirtualStore que represente uma plataforma de vendas
online. Essa classe deve ter funcionalidades para cadastrar produtos, gerar carrinho
de compras, aplicar descontos e calcular o valor total da compra.'''

class VirtualStore:
    def __init__(self):
        self.products = {}  # dictionary to store products with their prices
        self.cart = {}  # dictionary to store products in the cart with their quantities

    def addProduct(self, product_name, price):
        """Add a product to the store"""
        self.products[product_name] = price

    def addCart(self, product_name, quantity):
        """Add a product to the cart"""
        if product_name in self.products:
            if product_name in self.cart:
                self.cart[product_name] += quantity
            else:
                self.cart[product_name] = quantity
        else:
            print("Product not found in the store")

    @classmethod
    def createStore(cls):
        """Create a new VirtualStore instance"""
        return cls()

    def applyDiscount(self, discount_percentage):
        """Apply a discount to the total price"""
        total_price = self.totalPrice()
        discount_amount = (discount_percentage / 100) * total_price
        return total_price - discount_amount

    def totalPrice(self):
        """Calculate the total price of the products in the cart"""
        total_price = 0
        for product, quantity in self.cart.items():
            total_price += self.products[product] * quantity
        return total_price

    @staticmethod
    def calculateDiscount(total_price, discount_percentage):
        """Calculate the discount amount"""
        return (discount_percentage / 100) * total_price

    def viewCart(self):
        """Display the products in the cart"""
        print("Cart:")
        for product, quantity in self.cart.items():
            print(f"{product}: {quantity} x {self.products[product]} = {self.products[product] * quantity}")
        print(f"Total: {self.totalPrice()}")

def main():
    """Example usage of the VirtualStore class"""
    store = VirtualStore()
    store.addProduct("Product A", 10.99)
    store.addProduct("Product B", 5.99)
    store.addCart("Product A", 2)
    store.addCart("Product B", 3)
    store.viewCart()
    print(f"Total with 10% discount: {store.applyDiscount(10):.2f}")
main()