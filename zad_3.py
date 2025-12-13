class Property:

    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address


class House(Property):

    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f'Obiekt klasy House(Property) o polach: area: {self.area}, rooms: {self.rooms}, price: {self.price}, address: {self.address}, plot: {self.plot}'


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f'Obiekt klasy Flat(Property) o polach: area: {self.area}, rooms: {self.rooms}, price: {self.price}, address: {self.address}, floor: {self.floor}'


house_1 = House(120, 5, 870000, 'Chorzów, Ulica Zamkowa 2', 600)
flat_1 = Flat(75, 4, 350000, 'Bytom, Krasińskiego 3', 3)

print(house_1)
print(flat_1)
