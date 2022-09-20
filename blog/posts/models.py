from django.db import models


class Post(models.Model):
    body = models.TextField(max_length=200)
    created_at = models.DateTimeField('date published', auto_now=True)
