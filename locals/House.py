from locals.Property import Property

class House(Property):

    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f'Obiekt klasy House(Property) o polach: area: {self.area}, rooms: {self.rooms}, price: {self.price}, address: {self.address}, plot: {self.plot}'