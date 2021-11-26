from django.apps import AppConfig


class RobotsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'robots'
    
    def ready(self):
        try:
            from utils.csv_devices_reader import csv_reader
            csv_reader()
        
        except Exception as e:
            print(e.args)