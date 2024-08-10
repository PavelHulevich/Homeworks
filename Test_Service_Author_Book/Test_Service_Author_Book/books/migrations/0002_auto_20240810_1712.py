# Generated by Django 3.2.22 on 2024-08-10 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='fk_book_to_author',
        ),
        migrations.AddField(
            model_name='book',
            name='fk_book_to_author',
            field=models.ManyToManyField(to='authors.Author'),
        ),
    ]