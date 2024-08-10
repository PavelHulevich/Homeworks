# Generated by Django 3.2.22 on 2024-03-13 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=15)),
                ('status', models.CharField(max_length=7)),
                ('avatar', models.CharField(max_length=255)),
                ('profile', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('fk_user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile', unique=True)),
            ],
        ),
    ]
