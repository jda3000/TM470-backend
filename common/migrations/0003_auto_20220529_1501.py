# Generated by Django 3.2.10 on 2022-05-29 15:01

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beats', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0002_auto_20220424_1916'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='like',
            name='One one like per user per beat',
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('user', 'beat')},
        ),
    ]
