from django.db import models


class Tanks(models.Model):
    tank_name = models.CharField(max_length=10)
    tank_type = models.CharField(max_length=20)
    tank_description = models.TextField(max_length=100)
    damage_points = models.IntegerField()
    armor_points = models.IntegerField()
    speed = models.IntegerField()
    cost = models.IntegerField()
