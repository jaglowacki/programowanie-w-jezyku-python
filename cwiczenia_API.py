import requests

response1 = requests.get("https://api.openbrewerydb.org/v1/breweries/b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0")
response2 = requests.get("https://api.openbrewerydb.org/v1/breweries",'per_page=20')

if response1.status_code==200:
    print(response1.json())
else:
    print(f'Response 1.Coś poszło nie tak. Status code: {response1.status_code}')

if response2.status_code==200:
    print(f'Długość listy obiektów: {len(response2.json())}')
    print(response2.json())
    print('---------------------------------------------------------------------')
    lista=response2.json()
    for el in lista:
        print(el)
else:
    print(f'Response 2.Coś poszło nie tak. Status code: {response2.status_code}')

