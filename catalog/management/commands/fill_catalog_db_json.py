from django.core.management.base import BaseCommand
from catalog.models import ProductCategory, Product
from FarmMarketDjango.settings import BASE_DIR

import json
import os
import re


def fill_model_table(model, list):
    print('loading {} model'.format(model.model_name))
    for obj in list:
        new_model_object = model(**obj)
        new_model_object.save()
    print('model {} was loaded'.format(model.model_name))


def fill_db(data):
    fill_model_table(ProductCategory, data['ProductCategory'])
    product_data = data['Product']
    for product_dict in product_data:
        product_dict['category'] = ProductCategory.objects.get(name=product_dict['category'])

        if product_dict['img']:
            img_file_path = BASE_DIR
            for dir in re.split('/', product_dict['img']):
                img_file_path = os.path.join(img_file_path, dir)
            product_dict['img'] = img_file_path
        else:
            product_dict['img'] = ''

    fill_model_table(Product, product_data)


def get_json_path():
    json_path = os.path.join(BASE_DIR, 'json')

    print('\n\n{}:'.format(os.path.join(json_path, '')))
    for file_name in os.listdir(json_path):
        print('- {}'.format(file_name))
    print('Input path to JSON:')
    return os.path.join(json_path, input('{}'.format(os.path.join(json_path, ''))))


def objects_all_from_model(model):
    result = []
    for model_object in model.objects.all():
        result.append(model_object.get_dict())
    return {model.model_name: result}


class Command(BaseCommand):
    def handle(self, *args, **options):

        json_path = get_json_path()

        with open(json_path) as json_file:
            data_json = json.load(json_file)

        fill_db(data_json)


