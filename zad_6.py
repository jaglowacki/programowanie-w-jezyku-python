def laczenie(l1:list,l2:list)->list:
    lst=list(set(l1+l2))
    pot=[el**3 for el in lst]
    return pot

lista1=[1,2,3,4,8]
lista2=[6,2,7,8,11]


print(laczenie(lista1,lista2))
