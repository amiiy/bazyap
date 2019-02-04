from django.contrib import admin

from .models import Rubbish, Client, Order

admin.site.register(Order)
admin.site.register(Client)
admin.site.register(Rubbish)
