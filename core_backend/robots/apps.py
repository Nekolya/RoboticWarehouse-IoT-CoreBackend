from os import name
from django.apps import AppConfig


class RobotsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'robots'
    
    def ready(self):
        from .models import RobotStatus
        RobotStatus.objects.get_or_create(id=1, name="ACTIVE")
        RobotStatus.objects.get_or_create(id=2, name="CHARGING")
        RobotStatus.objects.get_or_create(id=3, name="ERROR")
        RobotStatus.objects.get_or_create(id=4, name="OFF")
        RobotStatus.objects.get_or_create(id=5, name="ORDERED")
