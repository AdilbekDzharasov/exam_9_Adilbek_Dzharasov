# Generated by Django 4.1.3 on 2022-11-26 06:25

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_photo_is_deleted'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='photo',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]