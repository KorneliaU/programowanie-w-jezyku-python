import magazine.utils

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def price_with_tax(self):
        return magazine.utils.calculate_tax(self.price)