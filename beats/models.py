from django.contrib.gis.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Beat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    route = models.LineStringField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.description}'
