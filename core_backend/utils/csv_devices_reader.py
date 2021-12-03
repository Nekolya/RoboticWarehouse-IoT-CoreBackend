import csv as csv_mod
from products.models import Product, Category
from zones.models import Location
from random import randint, seed


def csv_reader():
    with open('utils/devices.csv', newline='', encoding='utf-8') as file:

        csv = csv_mod.reader(file,  delimiter=',')
        print(csv)
        # print(file_obj.file.read("utf-8"))
        # print('\n---')
        counter = 1

        for line in csv:
            if "category id" in line:
                continue
            seed(1)
            Product.objects.get_or_create(id=counter, category=Category.objects.get(
                pk=line[0]), name=line[1], cost=line[2], location=Location.objects.get(pk=line[0]))
            # print("line", line[0], line[1], line[2])
            counter += 1
            # d.save()
