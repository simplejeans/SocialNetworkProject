from django.urls import path

from posts.views import PostViewSet, LikesAnalyticsAPIView

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'', PostViewSet)

urlpatterns = [

    path('likes/analytics/', LikesAnalyticsAPIView.as_view(), name='like_analytics')

]

urlpatterns += router.urls
