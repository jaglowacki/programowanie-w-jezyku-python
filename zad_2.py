def multiply2a(lista):
    nowa_lista=[]
    for el in lista:
        nowa_lista.append(el*2)
    return nowa_lista

def multiply2b(lista):
    nowa_lista=[el*2 for el in lista]
    return nowa_lista

print(multiply2a([11,22,33,44,55]))
print(multiply2b([11,22,33,44,55]))
