from django.contrib.gis.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    beat = models.ForeignKey('beats.Beat', on_delete=models.CASCADE, help_text='Comment on Beat')
    date_created = models.DateTimeField(auto_now_add=True)
    post = models.TextField()

    class Meta:
        ordering = ['-date_created']
