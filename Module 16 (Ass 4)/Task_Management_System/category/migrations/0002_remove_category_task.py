# Generated by Django 4.2.11 on 2024-03-27 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='task',
        ),
    ]