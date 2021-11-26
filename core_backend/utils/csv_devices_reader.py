import csv as csv_mod
from products.models import Product, Category


def csv_reader():
    a = [[1, "Процессоры", 1],
        [2, "Материнские платы", 1],
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
        [15, "Ноутбуки", 6]]
    
    for i in a:
        print(i)
        # c = Category.objects.get_or_create(id=i[0], name=i[1], weight=i[2])
    print('\n----')
    with open('utils/devices.csv', newline='', encoding='utf-8') as file:
        print('\n----')
        csv = csv_mod.reader(file,  delimiter=',')

        print(csv)
        print('\n----')
        # print(file_obj.file.read("utf-8"))
        # print('\n---')
        counter = 1

        for line in csv:
            if "category id" in line:
                continue
            # c = Product.objects.get_or_create(id=counter, category=line[0], name=line[1], cost=line[2])
            print("line", line[0], line[1], line[2])
            counter += 1
            # d.save()
