from django.contrib.auth import get_user_model
from django.db.models.functions import TruncDay
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from posts.models import Post, Like
from posts.permissions import IsAuthenticatedOrReadOnly
from posts.serializers import PostSerializer, LikesAnalyticsSerializer
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


class LikesAnalyticsAPIView(generics.ListAPIView):
    serializer_class = LikesAnalyticsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Like.objects.all()
    filter_backends = [DjangoFilterBackend, ]

    filterset_fields = {
        'created_at': ['gte', 'lte', 'exact', 'gt', 'lt']
    }

    def get_queryset(self):
        return Like.objects.all().annotate(date=TruncDay('created_at'))\
            .values('date').annotate(likes=Count('post')).order_by("-date")
