from django.shortcuts import render
from ..models import Product

def product(request,prod_id):

    id_prod = Product.objects.get(id=prod_id)
    selected_prod = id_prod
    all_prods = Product.objects.all()
    context = {
        'selected_prod': selected_prod,
        'all_prods': all_prods,
        'selected_prod' : id_prod
    }
    return render(request,'product.html', context)