from django.contrib.auth.models import User
from django.db import models


class UserActivity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_request = models.DateTimeField()
