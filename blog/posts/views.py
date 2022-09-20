from .models import Post

from rest_framework.viewsets import ModelViewSet

from .serializers import PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
