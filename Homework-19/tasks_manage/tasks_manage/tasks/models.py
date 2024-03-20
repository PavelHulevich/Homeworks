from django.db import models


class Tasks(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=255)
    file = models.CharField(max_length=255)
    status = models.CharField(max_length=17)
    date_of_create = models.CharField(max_length=25)
    deadline = models.CharField(max_length=25)
