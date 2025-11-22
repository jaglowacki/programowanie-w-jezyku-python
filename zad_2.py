def pomnoz2A(lista):
    nowa_lista=[]
    for el in lista:
        nowa_lista.append(el*2)
    return nowa_lista

def pomnoz2B(lista):
    nowa_lista=[el*2 for el in lista]
    return nowa_lista

print(pomnoz2A([11,22,33,44,55]))
print(pomnoz2B([11,22,33,44,55]))
