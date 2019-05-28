from django.test import TestCase

# Create your tests here.
import datetime

from django.test import TestCase

from .models import Smth


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