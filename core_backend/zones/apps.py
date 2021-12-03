from django.apps import AppConfig
from random import randint, seed

class ZonesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'zones'
    # def ready(self):
    #     try:
    #         from .models import AreaConnections, Area, Location, LocationType
    #         from products.models import Category, Product
            
    #         t20, created = Area.objects.get_or_create(id=20)
    #         t1, created = Area.objects.get_or_create(id=1)
    #         t2, created = Area.objects.get_or_create(id=2)
    #         t3, created = Area.objects.get_or_create(id=3)
    #         t4, created = Area.objects.get_or_create(id=4)
    #         t5, created = Area.objects.get_or_create(id=5)
    #         t6, created = Area.objects.get_or_create(id=6)
    #         t7, created = Area.objects.get_or_create(id=7)
    #         t8, created = Area.objects.get_or_create(id=8)
    #         t9, created = Area.objects.get_or_create(id=9)
    #         t10, created = Area.objects.get_or_create(id=10)
    #         t11, created = Area.objects.get_or_create(id=11)
    #         t12, created = Area.objects.get_or_create(id=12)
    #         t13, created = Area.objects.get_or_create(id=13)
    #         t14, created = Area.objects.get_or_create(id=14)
    #         t15, created = Area.objects.get_or_create(id=15)
    #         t16, created = Area.objects.get_or_create(id=16)
    #         t17, created = Area.objects.get_or_create(id=17)
    #         t18, created = Area.objects.get_or_create(id=18)
    #         t19, created = Area.objects.get_or_create(id=19)
            
            
    #         try:
    #             obj = AreaConnections.objects.get(area1=20, area2=1)
    #         except AreaConnections.DoesNotExist:
    #             obj = AreaConnections(area1=t20, area2=t1)
    #             obj.save()
            
            
    #         AreaConnections.objects.get_or_create(area1=t1, area2=t20)
    #         AreaConnections.objects.get_or_create(area1=t1, area2=t2)
    #         AreaConnections.objects.get_or_create(area1=t1, area2=t9)
            
    #         AreaConnections.objects.get_or_create(area1=t2, area2=t1)
    #         AreaConnections.objects.get_or_create(area1=t2, area2=t3)
    #         AreaConnections.objects.get_or_create(area1=t2, area2=t7)
            
    #         AreaConnections.objects.get_or_create(area1=t3, area2=t2)
    #         AreaConnections.objects.get_or_create(area1=t3, area2=t6)
    #         AreaConnections.objects.get_or_create(area1=t3, area2=t4)
    #         AreaConnections.objects.get_or_create(area1=t3, area2=t5)
            
    #         AreaConnections.objects.get_or_create(area1=t4, area2=t3)
            
    #         AreaConnections.objects.get_or_create(area1=t5, area2=t3)
            
    #         AreaConnections.objects.get_or_create(area1=t6, area2=t3)
            
    #         AreaConnections.objects.get_or_create(area1=t7, area2=t2)
    #         AreaConnections.objects.get_or_create(area1=t7, area2=t8)
            
    #         AreaConnections.objects.get_or_create(area1=t8, area2=t7)
            
    #         AreaConnections.objects.get_or_create(area1=t9, area2=t1)
    #         AreaConnections.objects.get_or_create(area1=t9, area2=t10)
    #         AreaConnections.objects.get_or_create(area1=t9, area2=t14)
            
    #         AreaConnections.objects.get_or_create(area1=t10, area2=t9)
    #         AreaConnections.objects.get_or_create(area1=t10, area2=t11)
            
    #         AreaConnections.objects.get_or_create(area1=t11, area2=t10)
    #         AreaConnections.objects.get_or_create(area1=t11, area2=t12)
    #         AreaConnections.objects.get_or_create(area1=t11, area2=t13)
            
    #         AreaConnections.objects.get_or_create(area1=t12, area2=t11)
    #         AreaConnections.objects.get_or_create(area1=t13, area2=t11)
            
    #         AreaConnections.objects.get_or_create(area1=t14, area2=t9)
    #         AreaConnections.objects.get_or_create(area1=t14, area2=t15)
    #         AreaConnections.objects.get_or_create(area1=t14, area2=t16)
            
    #         AreaConnections.objects.get_or_create(area1=t15, area2=t14)
            
    #         AreaConnections.objects.get_or_create(area1=t16, area2=t14)
    #         AreaConnections.objects.get_or_create(area1=t16, area2=t17)
    #         AreaConnections.objects.get_or_create(area1=t16, area2=t18)
            
    #         AreaConnections.objects.get_or_create(area1=t17, area2=t16)
            
    #         AreaConnections.objects.get_or_create(area1=t18, area2=t16)
    #         AreaConnections.objects.get_or_create(area1=t18, area2=t19)
            
    #         AreaConnections.objects.get_or_create(area1=t19, area2=t18)
            
    #         l1, created = LocationType.objects.get_or_create(id=1, defaults={'name': "Хранилище"})
    #         l2, created = LocationType.objects.get_or_create(id=2, defaults={'name': "Зона выдачи"})
    #         l3, created = LocationType.objects.get_or_create(id=3, defaults={'name': "Зарядка"})
    #         l4, created = LocationType.objects.get_or_create(id=4, defaults={'name': "Сортировочный центр"})
            
    #         Location.objects.get_or_create(id=1, area=t20, location_type=l1)
    #         Location.objects.get_or_create(id=2, area=t20, location_type=l1)
    #         Location.objects.get_or_create(id=3, area=t20, location_type=l1)
    #         Location.objects.get_or_create(id=4, area=t20, location_type=l1)
            
    #         Location.objects.get_or_create(id=5, area=t15, location_type=l1)
            
    #         Location.objects.get_or_create(id=6, area=t17, location_type=l1)
    #         Location.objects.get_or_create(id=7, area=t17, location_type=l1)
            
    #         Location.objects.get_or_create(id=8, area=t19, location_type=l1)
    #         Location.objects.get_or_create(id=9, area=t19, location_type=l1)
            
    #         Location.objects.get_or_create(id=10, area=t4, location_type=l1)
    #         Location.objects.get_or_create(id=11, area=t4, location_type=l1)
            
    #         Location.objects.get_or_create(id=12, area=t6, location_type=l1)
    #         Location.objects.get_or_create(id=13, area=t6, location_type=l1)
            
    #         Location.objects.get_or_create(id=14, area=t8, location_type=l1)
            
    #         Location.objects.get_or_create(id=15, area=t7, location_type=l1)
            
    #         Location.objects.get_or_create(id=16, area=t5, location_type=l2)
    #         Location.objects.get_or_create(id=17, area=t13, location_type=l3)
    #         Location.objects.get_or_create(id=18, area=t12, location_type=l4)
            
            
    #         a = [[1, "Процессоры", 1],
    #             [2, "Материнские платы", 1],
    #             [3, "Видеокарты", 3],
    #             [4, "Оперативная память", 1],
    #             [5, "Корпуса", 6],
    #             [6, "Блоки питания", 3],
    #             [7, "Системы охлаждения", 3],
    #             [8, "SSD", 1],
    #             [9, "HDD", 2],
    #             [10, "Звуковые карты", 1],
    #             [11, "Сетевые карты", 1],
    #             [12, "Гарнитура", 2],
    #             [13, "USB устройства", 3],
    #             [14, "ПК", 8],
    #             [15, "Ноутбуки", 6]]
            
    #         for i in a:
    #             # print(i)
    #             Category.objects.get_or_create(id=i[0], name=i[1], weight=i[2], location=Location.objects.get(pk=i[0]))
                
    #         from utils.csv_devices_reader import csv_reader
    #         csv_reader()
        
    #     except Exception as e:
    #         print(e.args)