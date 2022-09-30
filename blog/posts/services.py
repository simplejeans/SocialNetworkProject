from django.contrib.auth import get_user_model
from rest_framework.generics import get_object_or_404
from posts.models import Post



def like_post(post_id, user):
    post = get_object_or_404(Post, id=post_id)
    post.likes.add(user)


def unlike_post(post_id, user):
    post = get_object_or_404(Post, id=post_id)
    if post.likes.filter(id=user.id).exists():
        post.likes.remove(user.id)

