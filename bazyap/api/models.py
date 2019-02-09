from django.contrib.auth.models import AbstractUser
from django.db import models


class Client(AbstractUser):
    otp_code = models.IntegerField(null=True)
    first_name = models.CharField(max_length=64, null=True)
    last_name = models.CharField(max_length=64, null=True)
    token = models.CharField(max_length=512, null=True)

    def save(self, *args, **kwargs):
        print('saved this data:', args)
        super().save(*args, **kwargs)

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)
