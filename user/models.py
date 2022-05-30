from django.contrib.auth.models import AbstractUser
from django.db import models
from TM470_backend.storage_backends import PrivateMediaStorage


class User(AbstractUser):
    """ User model """

    email = models.EmailField(unique=True)
    image_thumb = models.ImageField(
        storage=PrivateMediaStorage,
        upload_to='images/users/',
        blank=True,
        null=True)

    terms_and_conditions = models.BooleanField(default=False)
