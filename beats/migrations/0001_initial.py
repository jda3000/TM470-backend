# Generated by Django 3.2.10 on 2021-12-29 00:26


from django.conf import settings
# from django.contrib.postgres.operations import CreateExtension

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion

# CreateExtension('postgis'),


class Migration(migrations.Migration):

    initial = True

    operations = [
        migrations.CreateModel(
            name='Beat',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('route', django.contrib.gis.db.models.fields.LineStringField(
                    blank=True, null=True, srid=4326)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
