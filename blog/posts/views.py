
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.viewsets import ModelViewSet

from posts.models import Post, Like
from posts.permissions import IsAuthenticatedOrReadOnly
from posts.serializers import PostSerializer, LikesSerializers

user = get_user_model()


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['post'])
    def like(self, request, pk):
        user = request.user
        post = get_object_or_404(Post, id=pk)
        post.likes.add(user)
        return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))

    @action(detail=True)
    def unlike(self, request, pk):
        user = request.user
        post = get_object_or_404(Post, id=pk)
        if post.likes.filter(id=user.id).exists():
            post.likes.remove(user.id)
        return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))




