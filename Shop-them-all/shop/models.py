from django.db import models

# Create your models here.

class Category(models.Model):
    def __str__(self):
        return self.name
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

class Shop(models.Model):
    def __str__(self):
        return self.name
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    xMap = models.IntegerField()
    yMap = models.IntegerField()

class Product(models.Model):
    def __str__(self):
        return self.name
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.FloatField(max_length=50)
    picturePath = models.CharField(max_length=300)
    color = models.CharField(max_length=50, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    size = models.CharField(max_length=5, null=True)
    description = models.CharField(max_length=500)
    id_vendor = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True)