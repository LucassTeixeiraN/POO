class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Discount:
    def apply(self, total_price):
        """Apply discount to the total price. Should be overridden by subclasses."""
        return total_price

class PercentageDiscount(Discount):
    def __init__(self, percentage):
        self.percentage = percentage

    def apply(self, total_price):
        discount_amount = (self.percentage / 100) * total_price
        return total_price - discount_amount