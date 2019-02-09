from django.urls import path
from . import views

# router = routers.DefaultRouter()
# router.register(r'groups', views.GroupSerializer)
# router.register(r'users', views.UserSerializer)

urlpatterns = [
    path('register', views.RegisterNumber),
    path('login', views.ValidateNumber),

]
