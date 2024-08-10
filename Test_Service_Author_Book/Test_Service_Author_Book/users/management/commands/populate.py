from django.core.management.base import BaseCommand
from users.models import Users, Profiles, Tasks
from faker import Faker
import random
import string
# from datetime import date
fake = Faker()


class Command(BaseCommand):
    help = 'Populates the database with fake data'

    def handle(self, *args, **kwargs):
        self.generate_tasks()
        self.generate_profile()
        self.generate_users()

    def generate_tasks(self, num_tasks=10) -> None:
        for _ in range(num_tasks):
            name = fake.user_name()
            description = fake.text(75)
            file = fake.text(75)
            status = random.choice(['ЗАПЛАНИРОВАНА', 'В РАБОТЕ',
                                    'ВЫПОЛНЕНА', 'ОТМЕНЕНА'])
            date_of_create = fake.date_time()
            deadline = fake.date_time()
            Tasks.objects.create(name=name, description=description, file=file, status=status,
                                 date_of_create=date_of_create, deadline=deadline)

    def generate_profile(self, num_users=5) -> None:
        for _ in range(num_users):
            phone = fake.random_int(81000000000, 89000000000)
            status = random.choice(['Обычный', 'Премиум'])
            avatar = fake.text(75)
            profile = fake.text(75)
            Profiles.objects.create(phone=phone, status=status, avatar=avatar, profile=profile)

    def generate_users(self, num_users=5) -> None:
        for i in range(num_users):
            profile_id = Profiles.objects.get(pk=i+1)
            name = fake.user_name()
            email = fake.email()
            password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
            Users.objects.create(name=name, email=email, password=password, fk_user_profile=profile_id)


