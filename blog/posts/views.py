from .models import Post

from rest_framework.viewsets import ModelViewSet

from .serializers import BlogSerializers


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = BlogSerializers
