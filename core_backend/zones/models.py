from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here
class LocationType(models.Model):
    """Model definition for LocationType."""

    name = models.CharField(max_length=255)

    class Meta:
        """Meta definition for LocationType."""

        verbose_name = 'LocationType'
        verbose_name_plural = 'LocationTypes'

    def __str__(self):
        """Unicode representation of LocationType."""
        pass

class Area(models.Model):
    """Model definition for Area."""
    

    class Meta:
        """Meta definition for Area."""

        verbose_name = 'Area'
        verbose_name_plural = 'Areas'

    def __str__(self):
        """Unicode representation of Area."""
        pass

# class AdjacentAreas(models.Model):
#     area_from = 
#     area_to = 

class Location(models.Model):
    """Model definition for Location."""
    area = models.ForeignKey('Area', on_delete=CASCADE, related_name='lacations')
    location_type = models.ForeignKey('LocationType', on_delete=CASCADE, related_name='lacations')
    name = models.CharField(max_length=255)

    class Meta:
        """Meta definition for Location."""

        verbose_name = 'Location'
        verbose_name_plural = 'Locations'

    def __str__(self):
        """Unicode representation of Location."""
        pass

class AreaConnections(models.Model):
    class Meta:
        unique_together = (('area1', 'area2'),)
    area1 = models.ForeignKey('Area', on_delete=CASCADE, related_name='lacations1')
    area2 = models.ForeignKey('Area', on_delete=CASCADE, related_name='lacations2')