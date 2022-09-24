
from posts.views import PostViewSet

from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register(r'', PostViewSet)

urlpatterns = []

urlpatterns += router.urls
