from django.db import models
from zones.models import Area, Location

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    weight = models.PositiveSmallIntegerField()
    category = models.ForeignKey(Area,
                                 related_name='devices',
                                 on_delete=models.CASCADE)


class Device(models.Model):
    name = models.CharField(max_length=255)
    cost = models.PositiveIntegerField()
    category = models.ForeignKey('Category',
                                 related_name='devices',
                                 on_delete=models.CASCADE)

    amount = models.PositiveIntegerField()
    location = models.ForeignKey(Location, related_name='devices', on_delete=models.CASCADE)