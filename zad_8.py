import argparse
import requests


class Brewery:

    def __init__(self, id: str = '', name: str = '', brewery_type: str = '', address_1: str = None, address_2: str = None,
                 address_3: str = None, city: str = '', state_province: str = '', postal_code: str = '', country: str = '',
                 longitude: float = 0.0, latitude: float = 0.0, phone: str = None, website_url: str = None, state: str = '',
                 street: str = None):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.address_1 = address_1
        self.address_2 = address_2
        self.address_3 = address_3
        self.city = city
        self.state_province = state_province
        self.postal_code = postal_code
        self.country = country
        self.longitude = longitude
        self.latitude = latitude
        self.phone = phone
        self.website_url = website_url
        self.state = state
        self.street = street

    def __str__(self):
        return f'Brewery(id={self.id}, name:={self.name}, brewery_type={self.brewery_type}, '\
                f'address_1={self.address_1}, address_2={self.address_2}, address_3={self.address_3}, '\
                f'city={self.city}, state_province={self.state_province}, postal_code={self.postal_code}, '\
                f'country={self.country}, longitude={self.longitude}, latitude={self.latitude}, '\
                f'phone={self.phone}, website_url={self.website_url}, state={self.state}, street={self.street})'

    @staticmethod
    def pobierz(adres: str, parametr: dict):
        response = requests.get(adres, parametr)
        if response.status_code == 200:
            # print(response.json())
            return response.json()
        else:
            print(f'Coś poszło nie tak. Status code: {response.status_code}')
            return None

    @staticmethod
    def przetworz(lista_browarow: list):
        lista_instancji = []
        for browar in lista_browarow:
            lista_instancji.append(Brewery(browar['id'], browar['name'], browar['brewery_type'], browar['address_1'],
                                           browar['address_2'], browar['address_3'], browar['city'],
                                           browar['state_province'], browar['postal_code'], browar['country'],
                                           browar['longitude'], browar['latitude'], browar['phone'],
                                           browar['website_url'], browar['state'], browar['street']))

        for instancja in lista_instancji:
            print(instancja)


parser = argparse.ArgumentParser()
parser.add_argument("--city", help="Wyświetla parametry browarów z podanego miasta")
args = parser.parse_args()
miasto = args.city

if miasto is not None:
    url = 'https://api.openbrewerydb.org/v1/breweries'
    params = {'by_city': miasto,
              'per_page': 20}
    lista_browarow = Brewery.pobierz(url, params)
else:
    url = 'https://api.openbrewerydb.org/v1/breweries'
    params = {'per_page': 20}
    lista_browarow = Brewery.pobierz(url, params)

if lista_browarow is not None:
    Brewery.przetworz(lista_browarow)
