from django.http import HttpResponse
from django.shortcuts import render
from ..models import Shop
from ..models import Product

def cart(request):

    context = {}
    if len(request.POST['cart_list']) > 0:
        ids = [request.POST['cart_list'].split(',')]
        all_selected_prod = Product.objects.filter(pk__in=ids[0])
        context = {
            'all_selected_prods': all_selected_prod,
        }
    return render(request, 'cart_page.html',context)

