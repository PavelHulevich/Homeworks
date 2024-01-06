class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        self.country = 'USA'
    def print_info(self):
        print(f'Name: {self.name}')
        print(f'Gender: {self.gender}')
        print(f'Age: {self.age}')
        print(f'Country: {self.country}')

person_1 = Person('Bob', 'Male', 20)
person_2 = Person('Нина', 'Женщина', 35)

print(person_1.name)
print(person_1.gender)
print(person_1.age)
print(person_1.country)
print(person_2.name)
print(person_2.gender)
print(person_2.age)
print(person_2.country)

person_1.print_info()

