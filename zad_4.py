def coDrugiElement(lista):
    for el in lista:
        if lista.index(el)%2==0:
            print(el)

lista_liczb=[i for i in range(10)]
coDrugiElement(lista_liczb)

