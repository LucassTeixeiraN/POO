'''Crie uma classe chamada VirtualStore que represente uma plataforma de vendas
online. Essa classe deve ter funcionalidades para cadastrar produtos, gerar carrinho
de compras, aplicar descontos e calcular o valor total da compra.'''


class VirtualStore:
    def __init__(self):
        self.products = {}  # dictionary to store products with their prices
        self.cart = {}  # dictionary to store products in the cart with their quantities
        self.customers = {}  # dictionary to store customers

    def addProduct(self, product_name, price):
        self.products[product_name] = price

    def addCart(self, product_name, quantity):
        if product_name in self.products:
            if product_name in self.cart:
                self.cart[product_name] += quantity
            else:
                self.cart[product_name] = quantity
        else:
            print("Product not found in the store")

    @classmethod
    def createStore(cls):
        return cls()

    def applyDiscount(self, discount_percentage):
        total_price = self.totalPrice()
        discount_amount = (discount_percentage / 100) * total_price
        return total_price - discount_amount

    def totalPrice(self):
        total_price = 0
        for product, quantity in self.cart.items():
            total_price += self.products[product] * quantity
        return total_price

    @staticmethod
    def calculateDiscount(total_price, discount_percentage):
        return (discount_percentage / 100) * total_price

    def viewCart(self):
        print("Cart:")
        for product, quantity in self.cart.items():
            print(f"{product}: {quantity} x {self.products[product]} = {self.products[product] * quantity}")
        print(f"Total: {self.totalPrice()}")

    def addCustomer(self, customer_id, customer_name):
        self.customers[customer_id] = Customer(customer_name)

    def getCustomer(self, customer_id):
        return self.customers.get(customer_id)


class Customer:
    def __init__(self, name):
        self.name = name
        self.payment_methods = {}  # dictionary to store payment methods

    def addPaymentMethod(self, payment_method_id, payment_method_type):
        self.payment_methods[payment_method_id] = PaymentMethod(payment_method_type)

    def getPaymentMethod(self, payment_method_id):
        return self.payment_methods.get(payment_method_id)


class PaymentMethod:
    def __init__(self, payment_method_type):
        self.payment_method_type = payment_method_type


def main():
    store = VirtualStore()
    store.addProduct("Product A", 10.99)
    store.addProduct("Product B", 5.99)
    store.addCart("Product A", 2)
    store.addCart("Product B", 3)
    store.viewCart()

    store.addCustomer("C001", "Lucas")
    customer = store.getCustomer("C001")
    customer.addPaymentMethod("PM001", "Credit Card")
    payment_method = customer.getPaymentMethod("PM001")
    print(f"Customer: {customer.name}, Payment Method: {payment_method.payment_method_type}")

    print(f"Total with 10% discount: {store.applyDiscount(10):.2f}")


main()
