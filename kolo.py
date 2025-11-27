from math import pi, pow
from decimal import Decimal, InvalidOperation


class Podaj:

    @staticmethod
    def input(tekst_zapytania):
        zle_znaki = True
        x = 0
        while zle_znaki:
            try:
                x = Decimal(input(tekst_zapytania))
                zle_znaki = False
            except InvalidOperation:
                zle_znaki = True
                print("Wprowadziłeś niepoprawną daną, spróbuj ponownie!")
        return float(x)


class Kolo:

    def __init__(self, r=0):  # konstruktor z możliwością ustawienie zmiennej prywatnej
        self.__r = Kolo.__spr_r(r)  # __r prywatne pole (zmienna), do którego obiekt nie ma dostępu

    @property  # zwraca własność 'property' - pola prywatnego
    def r(self):
        return self.__r

    @r.setter  # ustawia własność pola 'property' - pola prywatnego
    def r(self, value):
        self.__r = Kolo.__spr_r(value)

    def pole(self):  # metoda publiczna obliczająca pole powierzchni koła
        return pi * pow(self.__r, 2)

    def obwod(self):    # metoda publiczna obliczająca obwód koła
        return 2*pi*self.__r

    @staticmethod  # prywatna statyczna metoda sprawdzenia promienia
    def __spr_r(r):
        if r < 0:
            return 0
        else:
            return r

    @staticmethod  # publiczna statyczna metoda obliczania pola koła bez tworzenia obiektu
    def p(r):
        return pi * pow(r, 2)

    @staticmethod  # publiczna statyczna metoda obliczania obwodu koła bez tworzenia obiektu
    def o(r):
        return 2 * pi * r
