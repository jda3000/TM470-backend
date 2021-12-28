from django.contrib.postgres.operations import CreateExtension
from django.db import migrations
from django.contrib.gis.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Migration(migrations.Migration):

    operations = [
        CreateExtension('postgis'),
    ]


class Beat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    route = models.LineStringField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.description}'
