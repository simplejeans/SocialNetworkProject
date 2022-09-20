
from posts.views import PostViewSet
from blog.urls import urlpatterns
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register(r'posts', PostViewSet)


urlpatterns += router.urls
