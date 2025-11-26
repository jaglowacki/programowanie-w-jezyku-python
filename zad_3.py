def isBoolean(x:int) -> bool:
    if x%2==0:
        return True
    else:
        return False

a=4
parzysta=isBoolean(a)
if parzysta:
    print(f'Liczba x={a} jest parzysta')
else:
    print(f'Liczba x={a} nie jest parzysta')
