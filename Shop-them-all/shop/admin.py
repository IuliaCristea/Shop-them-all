from django.contrib import admin

from .models import Product
from .models import Shop
from .models import Category

admin.site.register(Product)
admin.site.register(Shop)
admin.site.register(Category)
