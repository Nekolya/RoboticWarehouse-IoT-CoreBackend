from os import name
from django.apps import AppConfig


class RobotsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'robots'
    
    def ready(self):
        from .models import RobotStatus, Robot
        from zones.models import Area

        try:
            r, s= RobotStatus.objects.get_or_create(id=1, name="ACTIVE")
            RobotStatus.objects.get_or_create(id=2, name="CHARGING")
            RobotStatus.objects.get_or_create(id=3, name="ERROR")
            RobotStatus.objects.get_or_create(id=4, name="OFF")
            RobotStatus.objects.get_or_create(id=5, name="ORDERED")
            
            Robot.objects.get_or_create(id=1, defaults={
                "model": "ROB-735472934",
                "charge": 100,
                "status": r,
                "area": Area.objects.get(pk=13)
                })
            Robot.objects.get_or_create(id=2, defaults={
                "model": "ROB-735472988",
                "charge": 100,
                "status": r,
                "area": Area.objects.get(pk=13)
                })
            Robot.objects.get_or_create(id=3, defaults={
                "model": "ROBO-835432481",
                "charge": 100,
                "status": r,
                "area": Area.objects.get(pk=13)
                })
            Robot.objects.get_or_create(id=4, defaults={
                "model": "RB-45433",
                "charge": 100,
                "status": r,
                "area": Area.objects.get(pk=13)
                })
        except Exception as e:
                print(e.args)