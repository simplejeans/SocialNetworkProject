from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.viewsets import ModelViewSet
from posts.models import Post
from posts.permissions import IsAuthenticatedOrReadOnly
from posts.serializers import PostSerializer
from posts.services import like_post, unlike_post

user = get_user_model()


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['post'])
    def like(self, request, pk):
        like_post(post_id=pk, user=request.user)
        return Response()

    @action(detail=True)
    def unlike(self, request, pk):
        unlike_post(post_id=pk, user=request.user)
        return Response()




