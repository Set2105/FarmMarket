from django.core.management.base import BaseCommand
from catalog.models import ProductCategory, Product
from FarmMarketDjango.settings import BASE_DIR

import json, os, time


def objects_all_from_model(model):
    result = []
    for model_object in model.objects.all():
        result.append(model_object.get_dict())
    return {model.model_name: result}


class Command(BaseCommand):
    def handle(self, *args, **options):
        file_name = input('Input json name, or palce space here to create automaticly:\n')
        if not file_name:
            file_name = 'catalog_dump_' + time.ctime().replace(' ', '_').replace(':', '_') + '.json'
        else:
            file_name += '.json'

        file_path = os.path.join(BASE_DIR, 'json', file_name)

        models_dict = {}

        models_dict.update(objects_all_from_model(ProductCategory))
        models_dict.update(objects_all_from_model(Product))

        with open(file_path, 'w') as json_file:
            json.dump(models_dict, fp=json_file, ensure_ascii=False)

        print('DB was successfully dumped in {}:'.format(file_path))
