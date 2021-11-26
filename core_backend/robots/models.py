from django.db import models
from django.db.models.fields import CharField
from zones.models import Area
from products.models import Product

class RobotStatus(models.Model):
    """Model definition for RobotStatus."""

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
    status = models.ForeignKey('RobotStatus', related_name='robots', on_delete=models.CASCADE)
    target_area = models.ForeignKey(Area, related_name='robots_target', on_delete=models.CASCADE)
    target_product = models.ForeignKey(Product, related_name='robots_target', on_delete=models.CASCADE) 
    area = models.ForeignKey(Area, related_name='robots', on_delete=models.CASCADE)
    charge = models.PositiveSmallIntegerField()
    product = models.ManyToManyField(Product, related_name='robots')

    class Meta:
        """Meta definition for Robot."""

        verbose_name = 'Robot'
        verbose_name_plural = 'Robots'
