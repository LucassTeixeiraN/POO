from product import Discount

class VirtualStore:
    def __init__(self):
        self.products = {}  # dictionary to store products by name
        self.cart = {}  # dictionary to store products in the cart with their quantities

    def addProduct(self, product):
        """Add a product to the store"""
        self.products[product.name] = product

    def addCart(self, product_name, quantity):
        """Add a product to the cart"""
        if product_name in self.products:
            if product_name in self.cart:
                self.cart[product_name] += quantity
            else:
                self.cart[product_name] = quantity
        else:
            print("Product not found in the store")

    def applyDiscount(self, discount: Discount):
        """Apply a discount to the total price"""
        total_price = self.totalPrice()
        return discount.apply(total_price)

    def totalPrice(self):
        """Calculate the total price of the products in the cart"""
        total_price = 0
        for product_name, quantity in self.cart.items():
            product = self.products[product_name]
            total_price += product.price * quantity
        return total_price

    def viewCart(self):
        """Display the products in the cart"""
        print("Cart:")
        for product_name, quantity in self.cart.items():
            product = self.products[product_name]
            print(f"{product.name}: {quantity} x {product.price} = {product.price * quantity}")
        print(f"Total: {self.totalPrice()}")
