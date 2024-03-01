from django.db import models
from vehicles.models import Tanks


class Players(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=10)
    date_joined = models.CharField(max_length=10)


class PlayerVehicles(models.Model):
    player_id = models.ForeignKey(Players, on_delete=models.CASCADE)
    vehicle_id = models.ForeignKey(Tanks, on_delete=models.CASCADE)
    experience_points = models.IntegerField()
