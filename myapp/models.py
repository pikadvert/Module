from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class MyUser(AbstractUser):
    birth_date = models.DateField()
    avatar = models.ImageField(blank=True, null=True)
    wallet = models.DecimalField(max_digits=7, decimal_places=2)


class Product(models.Model):
    productname = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField()
    image = models.CharField(max_length=5000, null=True, blank=True)
    quantity = models.IntegerField()

class Purchase(models.Model):
    bayer = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, related_name='bayer')
    purchase = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, related_name='purchases')
    quantity = models.IntegerField()

class Returns(models.Model):
    created_at = models.DateTimeField(default=timezone.now)