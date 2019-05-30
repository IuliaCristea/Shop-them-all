from django.test import TestCase

# Create your tests here.
import datetime

from django.test import TestCase, RequestFactory
from .models import Category
from .models import Product
from .views import iulia_views
from django import views

class SmthModelTests(TestCase):
    pass
    # def test1(self):
    #     """
    #     was_published_recently() returns False for questions whose pub_date
    #     is in the future.
    #     """
    #     smth = Smth();
    #     smth.ceva = "wtf?"
    #     self.assertIs(smth.ceva == "?wtf?", False)
    #
    #
    # def test2(self):
    #     """
    #     was_published_recently() returns False for questions whose pub_date
    #     is in the future.
    #     """
    #     smth = Smth();
    #     smth.ceva = "wtf?"
    #     self.assertIs(smth.ceva == "wtf?", True)

class Test(TestCase):
    def testSkirt(self):
        self.factory = RequestFactory()
        obj = Product.objects.filter(name="Skirt", color="Red")
        #obj.save()

        request = self.factory.get('/search?search=red+skirt')
        response = iulia_views.search(request)
        #print(response.context[-1]['search_resulted_shop'])
        self.assertEqual(response.status_code, 200)
        #self.assertIn(len(result), response.context[-1]['search_resulted_shop'])

    def testShirt(self):
        self.factory = RequestFactory()
        obj = Product.objects.filter(name="Shirt", color="Blue")
        # obj.save()

        request = self.factory.get('/search?search=shirt+blue')
        response = iulia_views.search(request)
        # print(response.context[-1]['search_resulted_shop'])
        self.assertEqual(response.status_code, 200)
        # self.assertIn(len(result), response.context[-1]['search_resulted_shop'])

    def testPants(self):
        self.factory = RequestFactory()
        obj = Product.objects.filter(name="Pants", color="Blue")
        # obj.save()

        request = self.factory.get('/search?search=pants+blue')
        response = iulia_views.search(request)
        # print(response.context[-1]['search_resulted_shop'])
        self.assertEqual(response.status_code, 200)
        # self.assertIn(len(result), response.context[-1]['search_resulted_shop'])
