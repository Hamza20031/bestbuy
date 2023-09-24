class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.promotion = None  # Added line for promotions

    def set_promotion(self, promotion):
        self.promotion = promotion

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity

    def buy(self, quantity):
        if quantity > self.quantity:
            raise Exception("Not enough stock available.")
        self.quantity -= quantity

        # Check if there's a promotion for the product and apply it
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)

        return self.price * quantity