
from rest_framework.generics import get_object_or_404
from posts.models import Post


def like_post(pk, request):
    user = request.user
    post = get_object_or_404(Post, id=pk)
    post.likes.add(user)


def unlike_post(pk, request):
    user = request.user
    post = get_object_or_404(Post, id=pk)
    if post.likes.filter(id=user.id).exists():
        post.likes.remove(user.id)

