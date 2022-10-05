from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Post(models.Model):
    body = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, through='Like', related_name='likes')

    def number_of_likes(self):
        return self.likes.count()


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)



