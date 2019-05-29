from django.http import HttpResponse
from django.shortcuts import render
from ..models import Product, Shop, Category

def home(request):
    return HttpResponse("Home Page")

def get_shop_list(request, shop_name):

    shop = Shop.objects.get(name=shop_name)
    all_prods = Product.objects.filter(id_vendor=shop)
    all_categories = [prod.category for prod in all_prods]
    all_categories = list(set(all_categories))
    context = {
        'shop': shop,
        'all_prods': all_prods,
        'all_categories': all_categories
    }
    return render(request,'shop_details.html', context)
