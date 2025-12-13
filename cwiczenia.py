class Car:
    def __init__(self, doors, color):
        self.doors = doors
        self.color = color
        self.hello()

    def __str__(self):
        return f'Samochód z drzwiami {self.doors}, z kolorem {self.color}'

    def hello(self):
        print(123)


my_car = Car(3, 'czerwony')

print(my_car)
print(dir(my_car))
