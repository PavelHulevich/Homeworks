from django.core.management.base import BaseCommand
from players.models import Players
from faker import Faker
import random
import string
from datetime import date
fake = Faker()


class Command(BaseCommand):
    help = 'Populates the database with fake data'

    def handle(self, *args, **kwargs):
        self.generate_players()

    def generate_players(self, num_users=20) -> None:
        for _ in range(num_users):
            username = fake.user_name()
            email = fake.email()
            password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
            date_joined = date
            Players.objects.create(username=username, email=email, password=password, date_joined=date_joined)
