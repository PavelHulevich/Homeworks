from django.db import models
from tasks.models import Tasks


STATUS = [('Обычный', 'Обычный'), ('Премиум', 'Премиум')]

class Profiles(models.Model):
    phone = models.CharField(max_length=15)
    # status = models.CharField(max_length=7)
    status = models.CharField(max_length=7, choices=STATUS, default='Обычный')
    avatar = models.CharField(max_length=255)
    profile = models.TextField(max_length=255)


class Users(models.Model):
    name = models.CharField(max_length=35, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    fk_user_profile = models.OneToOneField(Profiles, unique=True, on_delete=models.CASCADE)


class UsersTasks(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    task_id = models.ForeignKey(Tasks, on_delete=models.CASCADE)


