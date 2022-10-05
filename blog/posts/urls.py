from django.urls import path

from posts.views import PostViewSet, PostAnalyticsViewSet

from rest_framework.routers import SimpleRouter

router = SimpleRouter()


router.register(r'', PostViewSet)


urlpatterns = [

    path('analytics/', PostAnalyticsViewSet.as_view())

]

urlpatterns += router.urls
