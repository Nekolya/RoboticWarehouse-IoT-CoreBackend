import csv as csv_mod
import codecs
from products.models import Device, Category


def csv_reader(file):
    csv = csv_mod.reader(file.read().decode('utf-8').splitlines())

    print(csv)
    print('\n----')
    # print(file_obj.file.read("utf-8"))
    # print('\n---')
    cleared = line[0].replace('"', '')
    for line in csv:
        if "category id" in line:
            continue

        Device(name=cleared, cost=line[1], categoty=line[2])
        d.save()
        
if __name__ == '__main__':
    a = [[1, "Процессоры", 1],
        [2, "Материнские платы"], 1,
        [3, "Видеокарты", 3],
        [4, "Оперативная память", 1],
        [5, "Корпуса", 6],
        [6, "Блоки питания", 3],
        [7, "Системы охлаждения", 3],
        [8, "SSD", 1],
        [9, "HDD", 2],
        [10, "Звуковые карты", 1],
        [11, "Сетевые карты", 1],
        [12, "Гарнитура", 2],
        [13, "USB устройства", 3],
        [14, "ПК", 8],
        [15, "Ноутбуки"], 6]
    
    for i in a:
        c = Category.objects.get_or_create(id=i[0], name=i[1], weight=i[2])
    
    file = open('devices.csv', 'r')
    csv_reader(file)