from django.db import models

# Create your models here.
class tops(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.CharField(max_length=50)


class bottoms(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.CharField(max_length=50)

class shoes(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.IntegerField()


class accesories(models.Model):
  price = models.DecimalField(max_digits=6, decimal_places=2)
  type = models.CharField(max_length=50)


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
    