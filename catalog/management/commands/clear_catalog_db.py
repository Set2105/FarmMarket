from django.core.management.base import BaseCommand
from catalog.models import ProductCategory, Product
import random
import string


def clear_db():
    Product.objects.all().delete()
    ProductCategory.objects.all().delete()


class Command(BaseCommand):
    def handle(self, *args, **options):
        answer_letter = ''
        for i in range(8):
            answer_letter += random.choice(string.ascii_letters)

        is_ended = False
        while not is_ended:
            answer = input('For deleting all objects in DB input: {}\nTo abort operation input \'A\'\n'.format(answer_letter))

            if answer == answer_letter:
                is_ended = True
                clear_db()
                print('DB was successfully cleared !')

            if answer == 'A':
                is_ended = True
                print('Operation was aborted')
