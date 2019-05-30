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


    def testShirt(self):
        self.factory = RequestFactory()
        request = self.factory.get('/')
        response = iulia_views.home(request)
        self.assertEqual(response.status_code, 200)

