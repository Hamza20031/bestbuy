class Product:
    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity

    def buy(self, quantity):
        if quantity > self.quantity:
            raise Exception("Not enough stock available.")
        self.quantity -= quantity
        if self.quantity == 0:
            self.is_active = False
        return self.price * quantity, f"{quantity} unit(s) of {self.name} purchased."


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, 0)  # Quantity set to zero

    def buy(self, quantity):
        if quantity > 1:
            raise Exception("Non-stocked products can only be purchased one at a time.")
        return super().buy(quantity)

    def show(self):
        return f"{super().show()} (Non-Stocked Product)"


# For Limited Products
class LimitedProduct(Product):
    def __init__(self, name, price, quantity, max_purchase):
        super().__init__(name, price, quantity)
        self.max_purchase = max_purchase

    def buy(self, quantity):
        if quantity > self.max_purchase:
            raise Exception(f"Cannot buy more than {self.max_purchase} of this product at a time.")
        return super().buy(quantity)

    def show(self):
        return f"{super().show()} (Limited Product: Max Purchase {self.max_purchase})"
