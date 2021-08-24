#!/usr/bin/env python
# -*- coding: utf8 -*-

from catalog.models import ProductCategory


def catalog_menu(request):
    link_dict = {}
    link_dict.update({'Все товары': {"link": 'products:catalog', "argument": "0"}})
    for product in ProductCategory.objects.all():
        link_dict.update({product.name: {"link": "products:catalog", "argument": product.id}})
    link_dict.update({'TEST': {"link": 'test', "argument": None}})

    return {
        'catalog_menu': link_dict
    }
