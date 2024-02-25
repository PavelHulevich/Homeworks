from datetime import date
from faker import Faker
print(date.today())
fake = Faker('en')

a = fake.text(15)
print(a)
b = fake.random_int(0, 10)
print(b)