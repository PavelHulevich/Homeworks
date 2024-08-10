from django.db import models
from authors.models import Author


class Book(models.Model):
    title = models.CharField(max_length=35, unique=True)
    fk_book_to_author = models.OneToOneField(Author, unique=True, on_delete=models.CASCADE)