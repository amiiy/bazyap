from django.contrib.auth.models import AbstractUser
from django.db import models

SEX_TYPE = (
    (1, 'MALE'),
    (2, 'FEMALE'),
)


class Client(AbstractUser):
    otp_code = models.IntegerField(null=True)
    first_name = models.CharField(max_length=64, null=False)
    last_name = models.CharField(max_length=64, null=False)
    birthday = models.DateField(null=False, auto_now_add=True)
    sex = models.IntegerField(choices=SEX_TYPE, default=1)
    token = models.CharField(max_length=2048, null=True)

    def save(self, *args, **kwargs):
        print('saved this data:', args)
        super().save(*args, **kwargs)

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)
