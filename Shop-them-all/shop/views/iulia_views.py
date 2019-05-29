from django.http import HttpResponse
from django.shortcuts import render
from ..models import Shop
import json

def home(request):
    all_shops = Shop.objects.all()
    shops_mapping = {}
    for shop in all_shops:
        shops_mapping[shop.name] = [shop.xMap, shop.yMap]


    context = {
        'all_shops': all_shops,
        'shops_map': json.dumps(shops_mapping)
    }
    return render(request, 'home.html',context)