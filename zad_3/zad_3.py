class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address
class House(Property):
    def __init__(self, area, rooms: int, price, address, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (
            f"House | area: {self.area}, rooms: {self.rooms}, "
            f"price: {self.price}, address: {self.address}, plot: {self.plot}"
        )
class Flat(Property):
    def __init__(self, area, rooms: int, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor
    def __str__(self):
        return (
            f"Flat | area: {self.area}, rooms: {self.rooms}, "
            f"price: {self.price}, address: {self.address}, floor: {self.floor}"
        )
house = House(
    area=120,
    rooms=5,
    price=850000,
    address="Warszawa, ul. Zielona 10",
    plot=500
)

flat = Flat(
    area=60,
    rooms=3,
    price=520000,
    address="Kraków, ul. Kwiatowa 5",
    floor=3
)
print(house)
print(flat)