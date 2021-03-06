# Generated by Django 3.2.10 on 2022-06-07 21:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0003_auto_20220529_1501'),
    ]

    operations = [
        migrations.CreateModel(
            name='Following',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('recipient', models.ForeignKey(help_text='Person being followed', on_delete=django.db.models.deletion.CASCADE, related_name='being_followed_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(help_text='Person doing the following', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
    ]
