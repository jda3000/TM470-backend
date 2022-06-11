from django.contrib.gis.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Following(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text='Person doing the following')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='being_followed_by', help_text='Person being followed')
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']
        constraints = [
            models.UniqueConstraint(fields=['user', 'recipient'], name='user_recipient_constraint'),
        ]

    def __str__(self):
        return f'{self.user} is following {self.recipient}'