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


class Area(models.Model):
    """Model definition for Area."""

    class Meta:
        """Meta definition for Area."""

        verbose_name = 'Area'
        verbose_name_plural = 'Areas'

# class AdjacentAreas(models.Model):
#     area_from =
#     area_to =


class Location(models.Model):
    """Model definition for Location."""
    area = models.ForeignKey('Area', on_delete=CASCADE,
                             related_name='lacations')
    location_type = models.ForeignKey(
        'LocationType', on_delete=CASCADE, related_name='lacations')

    class Meta:
        """Meta definition for Location."""

        verbose_name = 'Location'
        verbose_name_plural = 'Locations'


class AreaConnections(models.Model):
    class Meta:
        constraints = [
        models.UniqueConstraint(fields=['area1', 'area2'], name='id')
    ]
    area1 = models.ForeignKey('Area', on_delete=CASCADE, related_name='area1')
    area2 = models.ForeignKey('Area', on_delete=CASCADE, related_name='area2')
