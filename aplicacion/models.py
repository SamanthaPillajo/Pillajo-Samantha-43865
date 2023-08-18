from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class tops(models.Model):
    name=models.CharField(max_length=50, blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.CharField(max_length=50, blank=True, null=True)
    contact = models.CharField(max_length=50, blank=True, null=True)
    photo = models.ImageField(upload_to ='products', null=True, blank=True)


class bottoms(models.Model):
    name=models.CharField(max_length=50, blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.CharField(max_length=50, blank=True, null=True)
    contact = models.CharField(max_length=50, blank=True, null=True)
    photo = models.ImageField(upload_to ='products', null=True, blank=True)

class shoes(models.Model):
    name=models.CharField(max_length=50, blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.IntegerField()
    contact = models.CharField(max_length=50, blank=True, null=True)
    photo = models.ImageField(upload_to ='products', null=True, blank=True)


class accessories(models.Model):
  name = models.CharField(max_length=50, blank=True, null=True)
  price = models.DecimalField(max_digits=6, decimal_places=2)
  size = models.CharField(max_length=50, blank=True, null=True)
  contact = models.CharField(max_length=50, blank=True, null=True)
  photo = models.ImageField(upload_to ='products', null=True, blank=True)



class Avatar(models.Model):
    image = models.ImageField(upload_to="avatars")
    user = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return f"{self.user} [{self.image}]"



    