# Generated by Django 3.2.22 on 2024-08-10 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
        ('books', '0006_auto_20240810_1817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book_to_author',
        ),
        migrations.AddField(
            model_name='book',
            name='fk_book_to_author',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='authors.author'),
        ),
    ]
