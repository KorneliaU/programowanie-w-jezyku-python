import magazine.utils


class Order:
    def __init__(self, products):
        self.products = products

    def total_tax(self):
        return sum(
            magazine.utils.calculate_tax(p.price)
            for p in self.products
        )
