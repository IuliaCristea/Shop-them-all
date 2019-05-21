from datetime import timezone, datetime

from django.db import models

# Create your models here.
from django.forms import forms


class Product(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=200)
    price = models.FloatField(max_length=50)
    picture = models.BinaryField()



class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Smth(models.Model):
    ceva = models.CharField(max_length=2)

class Iulia(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name