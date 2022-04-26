from django.contrib.gis.db import models
from django.contrib.auth import get_user_model

from TM470_backend.storage_backends import PrivateMediaStorage

User = get_user_model()


class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    beat = models.ForeignKey('beats.Beat', null=True, blank=True, on_delete=models.CASCADE, help_text='Kudos given to Beat')
    problem = models.ForeignKey('problems.Problem', null=True, blank=True, on_delete=models.CASCADE, help_text='Kudos given to Beat')
    date_created = models.DateTimeField(auto_now_add=True)
    file = models.FileField(
        storage=PrivateMediaStorage,
        upload_to='images/routes/',
        max_length=500) # upload to local server for now, will change to online cdn storage bucket later
    description = models.TextField(null=True, blank=True)