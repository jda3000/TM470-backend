from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.gis.geos import Point

from beats.models import Beat


@receiver(post_save, sender=Beat)
def introducer_created(sender, instance, created, **kwargs):
    if created and instance.route:
        print(instance.route.coords)
        instance.start_point = Point(instance.route.coords[0])
        instance.save()

