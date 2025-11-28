from kolo import *


class Walec(Kolo):

    def __init__(self, r, h=0):      # konstruktor z możliwością ustawienia zmiennych prywatnych
        super().__init__(r)          # dziedziczenie pól, właściwości i metod z klasy Kolo
        self.__h = Walec.__spr_h(h)

    def __str__(self):
        return 'Utworzenie obiektu klasy Walec o promieniu '+str(self.r)+' i wysokości '+str(self.__h)

    @property
    def h(self):
        return self.__h              # zwraca własność 'property' - pola prywatnego

    @h.setter
    def h(self, value):
        if value < 0:
            self.__h = 0
        else:
            self.__h = value

    @staticmethod                    # prywatna statyczna metoda sprawdzenia wysokości walca
    def __spr_h(h):
        if h < 0:
            return 0
        else:
            return h

    def powierzchnia(self):         # obliczenie powierzchni walca na podstawie danych obiektu
        return 2*Kolo.pole(self) + Kolo.obwod(self) * self.__h

    def objetosc(self):             # obliczenie objętości walca na podstawie danych obiektu
        return Kolo.pole(self) * self.__h

    @staticmethod  # publiczna statyczna metoda obliczania powierzchni walca bez tworzenia obiektu
    def pow(r, h):
        return 2*Kolo.p(r) + Kolo.o(r) * h

    @staticmethod  # publiczna statyczna metoda obliczania objętości walca bez tworzenia obiektu
    def obj(r, h):
        return Kolo.p(r) * h
