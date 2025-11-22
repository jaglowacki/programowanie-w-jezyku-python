def elParzyste(lista):
    for el in lista:
        if el%2==0:
            print(el)
lista_liczb=[i for i in range(10)]
elParzyste(lista_liczb)
