from django.http import HttpResponse
from django.shortcuts import render
from ..models import Product

def home(request):
    return HttpResponse("Home Page")

def get_prduct_details(request):

    all_prods = Product.objects.all()
    context = {
        'name': 'Bluza',
        'culoare' : 'rosie',
        'products': all_prods,
    }
    return render(request,'product_details.html', context)
