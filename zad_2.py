class Library:

    def __init__(self, city, street, zip_code, open_hours: str, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f'Obiekt klasy Library z polami: city:{self.city}, street:{self.street}, zip_code:{self.zip_code}, '\
               f'open_hours:{self.open_hours}, phone:{self.phone}'


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f'Obiekt klasy Employee z polami: first_name:{self.first_name}, last_name:{self.last_name}, hire_date:{self.hire_date}, '\
               f'birth_date:{self.birth_date}, city:{self.city}, street:{self.street}, zip_code:{self.zip_code}, phone:{self.phone}'


class Book:

    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f'Obiekt klasy Book z polami: [library:{self.library}], publication_date:{self.publication_date}, '\
               f'author_name:{self.author_name}, author_surname:{self.author_surname}, number_of_pages:{self.number_of_pages}'


class Order:

    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f'Obiekt klasy Order z polami: [employee:{self.employee}],[student:{self.student}],[books:{self.books}],order_date:{self.order_date}'


class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'Obiekt klasy Student z polami: first_name:{self.first_name}, last_name:{self.last_name}'


Biblioteka_1 = Library('Bytom', 'Konopnickiej', '41-909', '9-17', 322973456)
Biblioteka_2 = Library('Chorzów', 'Chorzowska', '41-505', '8-16', 323912345)

Pracownik_1 = Employee('Robert', 'Iksiński', '10.12.1998', '14.11.1980', 'Szombierki', 'Nowa', '41-801', '324568922')
Pracownik_2 = Employee('Andrzej', 'Matusiak', '11.09.2011', '23.08.1985', 'Siemianowice', 'Kwiatków', '41-678', '326567982')
Pracownik_3 = Employee('Janusz', 'Borowski', '10.08.2005', '21.07.1989', 'Katowice', 'Fiołków', '41-100', '324567282')

Ksiazka_1 = Book(Biblioteka_1, '20.12.1999', 'Tomasz', 'Kowalski', 234)
Ksiazka_2 = Book(Biblioteka_2, '21.11.2010', 'Adam', 'Nowak', 333)
Ksiazka_3 = Book(Biblioteka_1, '12.07.2009', 'Andrzej', 'Tur', 521)
Ksiazka_4 = Book(Biblioteka_1, '07.02.2005', 'Jarosław', 'Kogut', 432)
Ksiazka_5 = Book(Biblioteka_2, '06.05.2011', 'Sławomir', 'Kalecki', 121)

Student_1 = Student('Tomasz', 'Wiśniewski')
Student_2 = Student('Jeronim', 'Maj')
Student_3 = Student('Eugeniusz', 'Matejko')


Zamowienie_1 = Order(Pracownik_1, Student_1, Ksiazka_1, '01.02.2025')
Zamowienie_2 = Order(Pracownik_3, Student_2, Ksiazka_4, '12.05.2022')

print(Biblioteka_1)
print(Biblioteka_2)

print(Pracownik_1)
print(Pracownik_2)

print(Ksiazka_1)

print(Zamowienie_1)
print(Zamowienie_2)
