#from rest_framework import routers

from django.urls import path
from . import views


# router = routers.DefaultRouter()
# router.register(r'groups', views.GroupSerializer)
# router.register(r'users', views.UserSerializer)

urlpatterns = [
    path('', views.RegisterNumber),
]
