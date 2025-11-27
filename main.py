# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from walec import *


def wypisz_dane_kola(kolo, name):
    print(f"Kolo {name} ma promień: {kolo.r:.2f}, pole {kolo.pole():.2f}, obwód {kolo.obwod():.2f}")


def wypisz_dane_walca(walec, name):
    print(f"Walec {name} ma promień: {walec.r:.2f}, wysokość: {walec.h:.2f}, objętość {walec.objetosc():.2f}, "
          f"powierzchnię: {walec.powierzchnia():.2f}")


def wykonaj_program():
    k1 = Kolo(Podaj.input("Podaj promień koła k1.r="))
    wypisz_dane_kola(k1, "k1")
    print("UWAGA! Zmienimy promień: nowy=poprzedni*2")
    k1.r *= 2
    wypisz_dane_kola(k1, "k1")
    print(f"Pole koła o promieniu r=10 z metody statycznej klasy Kolo:  {Kolo.p(10):.2f}")
    print(f"Obwód koła o promieniu r=10 z metody statycznej klasy Kolo:  {Kolo.o(10):.2f}")
    print()

    w1 = Walec(Podaj.input("Podaj promień podstawy walce w1.r="), Podaj.input("Podaj wysokość walca w1.h="))
    wypisz_dane_walca(w1, "w1")
    print("UWAGA! Zmienimy promień walca: nowy=poprzedni*2")
    w1.r *= 2
    wypisz_dane_walca(w1, "w1")
    print(f"Objętość walca o promieniu r=10 i wysokości h=2 z metody statycznej klasy Walec:  {Walec.obj(10, 2):.2f}")
    print(f"Powierzchnia walca o promieniu r=10 i wysokości h=2 z metody statycznej klasy Walec:  {Walec.pow(10, 2):.2f}")


if __name__ == "__main__":
    wykonaj_program()


