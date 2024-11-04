from django.db import models
class product(models.Model):
    productid=models.CharField(max_length=64)
    productname=models.CharField(max_length=64)
    productprice=models.CharField(max_length=64)
class order(models.Model):
    orderno=models.CharField(max_length=64)
    orderdate=models.DateField(max_length=18)
