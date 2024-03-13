from django.db import models
from users.models import Users


class Tasks(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    file = models.BinaryField()
    status = models.CharField(max_length=15)
    date_of_create = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()


class UserTasks(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    task_id = models.ForeignKey(Tasks, on_delete=models.CASCADE)