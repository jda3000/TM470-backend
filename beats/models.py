from django.contrib.postgres.operations import CreateExtension
from django.db import migrations
from django.contrib.gis.db import models

# Create your models here.


class Migration(migrations.Migration):

    operations = [
        CreateExtension('postgis'),
    ]


class Beat(models.Model):
    description = models.TextField()
    coordinates = models.LineStringField(blank=True, null=True)

    def __str__(self):
        return f'{self.description}'