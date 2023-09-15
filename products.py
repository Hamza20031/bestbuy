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
        return self.price * quantity , f"{quantity} unit(s) of {self.name} purchased."