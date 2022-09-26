
from posts.views import PostViewSet, UserPostRelationView

from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register(r'', PostViewSet)
router.register(r'post_relation', UserPostRelationView)

urlpatterns = []

urlpatterns += router.urls
