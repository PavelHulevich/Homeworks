from django.core.management.base import BaseCommand
from achievements.models import Achievements, PlayerRanking
from vehicles.models import Tanks
from players.models import Players, PlayerVehicles
from faker import Faker
import random
import string
from datetime import date
fake = Faker()


class Command(BaseCommand):
    help = 'Populates the database with fake data'

    def handle(self, *args, **kwargs):
        self.generate_players()
        self.generate_tanks()
        self.generate_playervehicles()
        self.generate_achievements()
        self.generate_playerranking()

    def generate_players(self, num_users=20) -> None:
        for _ in range(num_users):
            username = fake.user_name()
            email = fake.email()
            password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
            date_joined = date.today()
            Players.objects.create(username=username, email=email, password=password, date_joined=date_joined)


    def generate_tanks(self, num_tanks=20) -> None:
        for _ in range(num_tanks):
            tank_name = fake.text(10)
            tank_type = fake.text(20)
            tank_description = fake.text(100)
            damage_points = fake.random_int(50, 1000)
            armor_points = fake.random_int(50, 200)
            speed = fake.random_int(10, 60)
            cost = fake.random_int(100, 1500)
            Tanks.objects.create(tank_name=tank_name, tank_type=tank_type, tank_description=tank_description,
                                   damage_points=damage_points, armor_points=armor_points, speed=speed, cost=cost)

    def generate_playervehicles(self, num_playervehicles=20) -> None:
        for _ in range(num_playervehicles):
            player_id = random.choice(Players.objects.all())
            vehicle_id = random.choice(Tanks.objects.all())
            experience_points = fake.random_int(50, 2000)
            PlayerVehicles.objects.create(player_id=player_id, vehicle_id=vehicle_id, experience_points=experience_points)


    def generate_achievements(self, num_achievements=20) -> None:
        for _ in range(num_achievements):
            player_id = random.choice(Players.objects.all())
            achievement_name = fake.text(50)
            achievement_description = fake.text(150)
            date_achieved = date.today()
            Achievements.objects.create(player_id=player_id, achievement_name=achievement_name,
                                        achievement_description=achievement_description, date_achieved=date_achieved)

    def generate_playerranking(self, num_playerranking=20) -> None:
        for _ in range(num_playerranking):
            player_id = random.choice(Players.objects.all())
            ranking_points = fake.random_int(1, 20)
            PlayerRanking.objects.create(player_id=player_id, ranking_points=ranking_points)
