class Product:
    def __init__(self, name, price, quantity):
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
        return self.price * quantity