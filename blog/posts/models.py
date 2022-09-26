from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Post(models.Model):
    body = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_posts')
    followers = models.ManyToManyField(User, through='UserPostRelation', related_name='followings_posts')


class UserPostRelation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    unlike = models.BooleanField(default=False)
