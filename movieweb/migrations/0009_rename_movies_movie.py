# Generated by Django 3.2.8 on 2021-10-26 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieweb', '0008_movies'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Movies',
            new_name='Movie',
        ),
    ]
