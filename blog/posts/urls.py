
from posts.views import PostViewSet, LikeAPIView

from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register(r'like', LikeAPIView)
router.register(r'', PostViewSet)


urlpatterns = []

urlpatterns += router.urls
