from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    def ready(self):
        try:
            from utils.robots_connection import RobotsConnection
            r = RobotsConnection()
            import asyncio
            loop = asyncio.get_event_loop()
            loop.run_until_complete(r.main())
            
        except Exception as e:
            pass