from abc import ABC, abstractmethod

# Abstract Promotion class
class Promotion(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass

# Concrete Promotion classes
class PercentageDiscountPromotion(Promotion):

    def __init__(self, percentage):
        super().__init__("Percentage Discount")
        self.percentage = percentage

    def apply_promotion(self, product, quantity):
        return product.get_price() * quantity * (1 - (self.percentage / 100))

class SecondItemAtHalfPricePromotion(Promotion):

    def __init__(self):
        super().__init__("Second Item at Half Price")

    def apply_promotion(self, product, quantity):
        full_price_items = quantity // 2 + quantity % 2
        half_price_items = quantity // 2
        return product.get_price() * (full_price_items + 0.5 * half_price_items)

class BuyTwoGetOneFreePromotion(Promotion):

    def __init__(self):
        super().__init__("Buy 2 Get 1 Free")

    def apply_promotion(self, product, quantity):
        payable_quantity = 2 * (quantity // 3) + quantity % 3
        return product.get_price() * payable_quantity
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
        self.promotion = None

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity

    def set_promotion(self, promotion):
        self.promotion = promotion

    def buy(self, quantity):
        if quantity > self.quantity:
            raise Exception("Not enough stock available.")
        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity
        self.quantity -= quantity
        if self.quantity == 0:
            self.is_active = False
        return total_price , f"{quantity} unit(s) of {self.name} purchased."
    def show(self):
        promo_str = f"Current Promotion: {self.promotion.name}" if self.promotion else "No current promotion"
        return f"{self.name}: Price: {self.price}, Quantity: {self.quantity}. {promo_str}"

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
