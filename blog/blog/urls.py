
from django.urls import path, include
from django.contrib import admin
from rest_framework_simplejwt.views import TokenVerifyView, TokenRefreshView, TokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/users/", include("users.urls")),

]
