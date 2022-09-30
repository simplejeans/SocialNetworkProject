
from django.urls import path, include
from django.contrib import admin

from posts.views import PostViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/posts/', include('posts.urls')),
    path("api/users/", include("users.urls")),


]
