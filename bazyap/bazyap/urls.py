from django.contrib import admin
from django.urls import include, path
from rest_framework_jwt.views import obtain_jwt_token


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('login', obtain_jwt_token),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),

]