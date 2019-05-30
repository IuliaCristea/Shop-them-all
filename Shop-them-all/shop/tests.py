from django.test import TestCase

# Create your tests here.
import datetime

from django.test import TestCase, RequestFactory
from .models import Category
from .models import Product, Shop, Category
from .views import iulia_views
from django import views


class Test(TestCase):

    def testSearchResponse(self):
        self.factory = RequestFactory()
        request = self.factory.get('/search?search=red+skirt')
        response = iulia_views.search(request)
        self.assertEqual(response.status_code, 200)


    def testHomeResponse(self):
        self.factory = RequestFactory()
        request = self.factory.get('/')
        response = iulia_views.home(request)
        self.assertEqual(response.status_code, 200)

    def testShopCreation(self):
        shop = Shop(name="magazin", xMap=0, yMap=0)
        shop.save();
        self.assertEqual(1, len(Shop.objects.all()))

    def testCategoryCreation(self):
        cat = Category(name="category")
        cat.save();
        self.assertEqual(1, len(Category.objects.all()))

    def testProductCreation(self):
        cat = Category(name="category1")
        cat.save();
        shop = Shop(name="magazin1", xMap=0, yMap=0)
        shop.save();
        prod = Product(name="Product", price=10, picturePath="empty", color="red", category=cat, size="s",
                       description="Noice", id_vendor=shop)
        prod.save();
        self.assertEqual(1, len(Category.objects.all()))




