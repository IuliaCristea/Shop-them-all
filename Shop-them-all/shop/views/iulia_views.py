from django.http import HttpResponse
from django.shortcuts import render
from ..models import Shop, Product
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


def search(request):
    all_shops = Shop.objects.all()
    shops_mapping = {}
    for shop in all_shops:
        shops_mapping[shop.name] = [shop.xMap, shop.yMap]

    context = {
        'all_shops': all_shops,
        'shops_map': json.dumps(shops_mapping),
    }

    searchResult = search_internal(request.GET['search'])
    if(len(searchResult) != 0):
        context['search_resulted_shop'] = searchResult

    return render(request, 'home.html', context)

def search_internal(searchText):

    if len(searchText) > 0:
        searchElements = searchText.split(" ");
        firsFilter = Product.objects.filter(name__contains=searchElements[1].lower())
        secondFilter = list(
            set([prod.id_vendor.name for prod in firsFilter if prod.color.lower() == searchElements[0].lower()]))
        if len(secondFilter) == 0:
            secondFilter = list(set([prod.id_vendor.name for prod in firsFilter]))

        return json.dumps(secondFilter)

    return []