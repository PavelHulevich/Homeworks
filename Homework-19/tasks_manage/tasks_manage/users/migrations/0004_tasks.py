# Generated by Django 3.2.22 on 2024-03-19 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_profile_profiles'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(max_length=255)),
                ('file', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=15)),
                ('date_of_create', models.DateTimeField()),
                ('deadline', models.DateTimeField()),
            ],
        ),
    ]
