# Generated by Django 3.0.6 on 2020-06-20 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goals',
            name='author',
        ),
    ]
