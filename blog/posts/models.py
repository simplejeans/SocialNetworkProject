from django.contrib.auth import get_user_model
from django.db import models


user = get_user_model()


class Post(models.Model):
    body = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(user, on_delete=models.CASCADE)

