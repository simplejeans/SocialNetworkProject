from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet

from posts.models import Post, Like
from posts.permissions import IsAuthenticatedOrReadOnly
from posts.serializers import PostSerializer, LikesSerializers


user = get_user_model()


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class LikeAPIView(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Like.objects.all()
    serializer_class = LikesSerializers
    lookup_field = 'post'






