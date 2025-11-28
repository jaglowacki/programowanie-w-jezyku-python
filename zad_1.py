class Student:
    def __init__(self, name:str , marks:int ):
        self.name = name
        self.marks = marks

    def isPassed(self)->bool:
        return self.marks > 50

Student_1=Student('Piotr', 87)
Student_2=Student('Marcin',35)

print(f'Student {Student_1.name} przekroczył próg: {Student_1.isPassed()}')
print(f'Student {Student_2.name} przekroczył próg: {Student_2.isPassed()}')
