from django.db import models
from players.models import Players


class Achievements(models.Model):
    player_id = models.ForeignKey(Players, on_delete=models.CASCADE)
    achievement_name = models.CharField(max_length=50)
    achievement_description = models.TextField()
    date_achieved = models.DateField()


class PlayerRanking(models.Model):
    player_id = models.ForeignKey(Players, on_delete=models.CASCADE)
    ranking_points = models.IntegerField()


