from django.db import models

STATUS = [('Запланирована ', 'Запланирована'), ('В работе', 'В работе'),
          ('Выполнена', 'Выполнена'), ('Отменена', 'Отменена')]


class Tasks(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    status = models.CharField(max_length=17, choices=STATUS, default='Запланирована')
    date_of_create = models.DateTimeField()
    deadline = models.DateField()
