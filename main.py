import magazine.Product

from locals.House import House
import locals.Flat

house_1 = House(120, 5, 870000, 'Chorzów, Ulica Zamkowa 2', 600)
flat_1 = locals.Flat.Flat(75, 4, 350000, 'Bytom, Krasińskiego 3', 3)

print(house_1)
print(flat_1)