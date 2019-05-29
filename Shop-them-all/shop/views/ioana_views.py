from django.http import HttpResponse
from django.shortcuts import render
from ..models import Shop
from ..models import Product

def cart(request):
    all_shops = Shop.objects.all()
    all_selected_prod = Product.objects.all()
    context = {
        'all_shops': all_shops,
        'all_selected_prods': all_selected_prod,
    }
    return render(request, 'cart_page.html',context)