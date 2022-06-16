
from django.contrib.gis.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

#
# from django.contrib.postgres.operations import CreateExtension
# from django.db import migrations
# # add this to the initial migration to install postgis extension
# class Migration(migrations.Migration):
#     operations = [
#         CreateExtension('postgis'),
#     ]


class Beat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    route = models.LineStringField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True) # allow blank end time as may want to save beat before finishing it (i.e. to resume at a later time/date)
    litter_collected_amount = models.PositiveSmallIntegerField(null=True, blank=True)
    private = models.BooleanField(default=False)
    start_point = models.PointField(null=True, blank=True)


    def __str__(self):
        return f'{self.description}'



