# Generated by Django 3.2.22 on 2024-03-13 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=255)),
                ('file', models.BinaryField()),
                ('status', models.CharField(max_length=15)),
                ('date_of_create', models.DateTimeField(auto_now_add=True)),
                ('deadline', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='UserTasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.tasks')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.users')),
            ],
        ),
    ]