from django.contrib import admin
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.admin import UserAdmin

from .models import Client


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Client


class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number',)}),
    )


admin.site.register(Client, MyUserAdmin)
