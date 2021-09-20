from django.db import models

# Create your models here.
class Device(models.Model):
    name = models.CharField(max_length=255)
    cost = models.PositiveIntegerField()
    category = models.ForeignKey('Category',
                                 related_name='devices',
                                 on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    weight = models.PositiveSmallIntegerField()
    