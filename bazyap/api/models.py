from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Client(AbstractUser):
    otp_code = models.IntegerField(null=True)
    phone_number = models.CharField(unique=True, max_length=15)
    first_name = models.CharField(max_length=64, null=True)
    last_name = models.CharField(max_length=64, null=True)
    token = models.CharField(max_length=512, null=True)
