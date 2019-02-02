from django.contrib.auth.models import User
from django.db import models


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


#    type = models.CharField(max_length=1, choices=)



class Rubbish(models.Model):
    RUBBISH_TYPES = (
        ('GL', 'GLASS'),
        ('BR', 'BREAD'),
        ('ME', 'METAL'),
        ('AL', 'ALOMINUM'),
        ('PA', 'PAPER'),
    )
    type = models.CharField(max_length=2, choices=RUBBISH_TYPES)


class Order(models.Model):
    user = models.ForeignKey(Client, on_delete=models.CASCADE)
    entity = models.ManyToManyField(Rubbish)
