from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        try:
            from .models import AuthUser, OrderStatus
            from os import environ
            try:
                OrderStatus.objects.get_or_create(id=1, name="ACTIVE")
                OrderStatus.objects.get_or_create(id=2, name="ASSEMBLY")
                OrderStatus.objects.get_or_create(id=3, name="FINISHED")
                OrderStatus.objects.get_or_create(id=4, name="CANCELED")
                AuthUser.objects.get(username=environ.get('ADMIN_LOGIN'))
                
            except Exception as e:
                try:
                    AuthUser.objects.create_superuser(username=environ.get('ADMIN_LOGIN'),
                                                    password=environ.get('ADMIN_PASSWORD'), name="Ольга", surename="Быковская")
                except Exception as exc:
                    print(exc.args)
            
            
            from utils.robots_connection import RobotsConnection
            r = RobotsConnection()
            import asyncio
            loop = asyncio.get_event_loop()
            loop.run_until_complete(r.main())

        except Exception as e:
            pass
