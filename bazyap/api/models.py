from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.db.models.signals import post_save

SEX_TYPE = (
    (1, 'MALE'),
    (2, 'FEMALE'),
)

USER_TYPE = (
    (1, 'BASIC'),
    (2, 'AGENT'),
    (3, 'BUSINESS'),
)


class Client(AbstractUser):
    otp_code = models.IntegerField(null=True)
    last_name = models.CharField(max_length=64, null=False)
    sex = models.IntegerField(choices=SEX_TYPE, default=1)
    token = models.ForeignKey(Token, on_delete=models.CASCADE, null=True)
    type = models.IntegerField(choices=USER_TYPE, default=1)
    is_valid_phone_number = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        print('saved this data:', args)
        super().save(*args, **kwargs)

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
