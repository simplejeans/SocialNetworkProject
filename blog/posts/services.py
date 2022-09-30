from django.contrib.auth import get_user_model
from rest_framework.generics import get_object_or_404
from posts.models import Post, Like


def like_post(post_id, user):
    post = get_object_or_404(Post, id=post_id)
    Like.objects.get_or_create(post=post, user=user)


def unlike_post(post_id, user):
    post = get_object_or_404(Post, id=post_id)
    Like.objects.filter(post=post, user=user).delete()

