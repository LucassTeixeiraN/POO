from virtualStore import VirtualStore
from product import Product
from product import PercentageDiscount
def main():
    """Example usage of the VirtualStore class"""
    store = VirtualStore()
    store.addProduct(Product("Product A", 10.99))
    store.addProduct(Product("Product B", 5.99))
    store.addCart("Product A", 2)
    store.addCart("Product B", 3)
    store.viewCart()

    # Applying a percentage discount
    discount = PercentageDiscount(10)
    print(f"Total with 10% discount: {discount.apply(store.totalPrice()):.2f}")

main()