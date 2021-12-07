from os import name
from django.db import models
from zones.models import Area
from products.models import Product
from django.contrib.postgres.fields import ArrayField


class RobotStatus(models.Model):
    """Model definition for RobotStatus."""
    name = models.CharField(max_length=20)
    # TODO: Define fields here

    class Meta:
        """Meta definition for RobotStatus."""

        verbose_name = 'RobotStatus'
        verbose_name_plural = 'RobotStatuss'


# Create your models here.
class Robot(models.Model):
    """Model definition for Robot."""
    id = models.IntegerField(primary_key=True)
    model = models.CharField(max_length=50)
    status = models.ForeignKey(
        'RobotStatus', related_name='robots', on_delete=models.CASCADE)
    area = models.ForeignKey(
        Area, related_name='robots', on_delete=models.CASCADE, null=True, default=None)
    way = ArrayField(models.IntegerField(), null=True)
    charge = models.PositiveSmallIntegerField()
    product = models.ForeignKey(
        Product, related_name='robots', on_delete=models.CASCADE, null=True)
    took = models.BooleanField(default=False)

    class Meta:
        """Meta definition for Robot."""

        verbose_name = 'Robot'
        verbose_name_plural = 'Robots'

