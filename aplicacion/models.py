from django.db import models

# Create your models here.
class tops(models.Model):
    name=models.CharField(max_length=50, blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.CharField(max_length=50, blank=True, null=True)
    contact = models.CharField(max_length=50, blank=True, null=True)


class bottoms(models.Model):
    name=models.CharField(max_length=50, blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.CharField(max_length=50, blank=True, null=True)
    contact = models.CharField(max_length=50, blank=True, null=True)

class shoes(models.Model):
    name=models.CharField(max_length=50, blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.IntegerField()
    contact = models.CharField(max_length=50, blank=True, null=True)


class accessories(models.Model):
  name = models.CharField(max_length=50, blank=True, null=True)
  price = models.DecimalField(max_digits=6, decimal_places=2)
  size = models.CharField(max_length=50, blank=True, null=True)
  contact = models.CharField(max_length=50, blank=True, null=True)


 #TALLAS = (
        #(1, "Extra Small"),
       # (2, "Small"),
        #(3, "Medium"),
        #(4, "Large"),
        #(5, "Extra Large")#

          ##TIPOS = (
        #(1, "Collar"),
        #(2, "Bracelete"),
        #(3, "Bag"),
        #(4, "Belt"),
        #(5, "Hat"),
    