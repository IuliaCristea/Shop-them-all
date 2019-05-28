from django.http import HttpResponse
from django.shortcuts import render
from ..models import Shop

def home(request):
    all_shops = Shop.objects.all()
    context = {
        'all_shops': all_shops
    }
    return render(request, 'home.html',context)