from django.contrib.gis.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Problem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    location = models.PointField()
    beat = models.ForeignKey('beats.Beat', null=True, blank=True, on_delete=models.CASCADE, help_text='Recorded on Beat')