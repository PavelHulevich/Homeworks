from django.db import models


class Profile(models.Model):
    phone = models.CharField(max_length=15)
    status = models.CharField(max_length=7)
    avatar = models.CharField(max_length=255)
    profile = models.TextField(max_length=255)


class Users(models.Model):
    name = models.CharField(max_length=35, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    fk_user_profile = models.ForeignKey(Profile, unique=True, on_delete=models.CASCADE)






