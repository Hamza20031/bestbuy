class Store:
    def __init__(self, products):
        self.products = products

    def get_all_products(self):
        for product in self.products:
            print(f"{product.name} - Price: {product.get_price()} - Quantity: {product.get_quantity()}")

    def get_total_quantity(self):
        return sum(product.get_quantity() for product in self.products)