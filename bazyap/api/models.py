from django.contrib.auth.models import User

from django.db import models


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    opt = models.IntegerField()
    phone_number = models.CharField(unique=True, max_length=12)


class Rubbish(models.Model):
    RUBBISH_TYPES = (
        ('GL', 'GLASS'),
        ('BR', 'BREAD'),
        ('ME', 'METAL'),
        ('AL', 'ALOMINUM'),
        ('PA', 'PAPER'),
    )
    type = models.CharField(max_length=2, choices=RUBBISH_TYPES)
    value = models.IntegerField(default=0)


class Order(models.Model):
    user = models.ForeignKey(Client, on_delete=models.CASCADE)
    cart_rubbish = models.ManyToManyField(Rubbish)
    lat = models.DecimalField(max_digits=8, decimal_places=3)
    long = models.DecimalField(max_digits=8, decimal_places=3)
