from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        """This abstract method will calculate the discounted price based on the promotion."""
        pass


class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self._percent = percent

    def apply_promotion(self, product, quantity):
        discount = product.price * (self._percent / 100)
        return (product.price - discount) * quantity


class SecondHalfPrice(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        full_price_items = (quantity // 2) + (quantity % 2)
        half_price_items = quantity // 2
        return (full_price_items * product.price) + (half_price_items * product.price * 0.5)


class ThirdOneFree(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        free_items = quantity // 3
        paid_items = quantity - free_items
        return paid_items * product.price