from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here
class AreaType(models.Model):
    """Model definition for AreaType."""

    name = models.CharField(max_length=255)

    class Meta:
        """Meta definition for AreaType."""

        verbose_name = 'AreaType'
        verbose_name_plural = 'AreaTypes'

    def __str__(self):
        """Unicode representation of AreaType."""
        pass

class Area(models.Model):
    """Model definition for Area."""
    area_type = models.ForeignKey('AreaType', on_delete=CASCADE, related_name='areas')
    # TODO: Define fields here

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

    # TODO: Define fields here

    class Meta:
        """Meta definition for Location."""

        verbose_name = 'Location'
        verbose_name_plural = 'Locations'

    def __str__(self):
        """Unicode representation of Location."""
        pass
