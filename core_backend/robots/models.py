from django.db import models
from django.db.models.fields import CharField
from zones.models import Area
from products.models import Device

class RobotStatus(models.Model):
    """Model definition for RobotStatus."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for RobotStatus."""

        verbose_name = 'RobotStatus'
        verbose_name_plural = 'RobotStatuss'

    def __str__(self):
        """Unicode representation of RobotStatus."""
        pass

# Create your models here.
class Robot(models.Model):
    """Model definition for Robot."""
    id = models.IntegerField()
    model = models.CharField(max_length=50)
    status = models.ForeignKey('RobotStatus', related_name='robots', on_delete=models.CASCADE)
    target_area = models.ForeignKey(Area, related_name='robots_target', on_delete=models.CASCADE)
    target_device = models.ForeignKey(Device, related_name='robots', on_delete=models.CASCADE) 
    area = models.ForeignKey(Area, related_name='robots', on_delete=models.CASCADE)
    charge = models.PositiveSmallIntegerField(max_value=100)
    devices = models.ManyToManyField(Device, related_name='robots')

    class Meta:
        """Meta definition for Robot."""

        verbose_name = 'Robot'
        verbose_name_plural = 'Robots'

    def __str__(self):
        """Unicode representation of Robot."""
        pass
