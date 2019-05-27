from datetime import timezone, datetime

from django.db import models

# Create your models here.


class Product(models.Model):
    def __str__(self):
        return self.name
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.FloatField(max_length=50)
    picturePath = models.CharField(max_length=300)
    description = models.CharField(max_length=500)

class Buys(models.Model):
    class Meta:
        unique_together = (('id_product', 'id_user'),)
    id_product = models.IntegerField()
    id_user = models.IntegerField()

class Vendor(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

class Sells(models.Model):
    class Meta:
        unique_together = (('id_product', 'id_vendor'),)
    id_product = models.IntegerField()
    id_vendor = models.IntegerField()



class Smth(models.Model):
    ceva = models.CharField(max_length=2)

class Iulia(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name