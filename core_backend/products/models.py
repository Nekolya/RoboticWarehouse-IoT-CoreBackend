from django.db import models
from zones.models import Area, Location

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    weight = models.PositiveSmallIntegerField()
    location = models.ForeignKey(Location,
                                 related_name='categories',
                                 on_delete=models.CASCADE)


class Product(models.Model):
    name = models.CharField(max_length=255)
    cost = models.PositiveIntegerField()
    category = models.ForeignKey('Category',
                                 related_name='products',
                                 on_delete=models.CASCADE)

    location = models.ForeignKey(
        Location, related_name='products', on_delete=models.CASCADE)
