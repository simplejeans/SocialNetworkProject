from django.contrib import admin
from django.contrib.admin import ModelAdmin

from posts.models import Post, Like
from users.models import UserActivity


@admin.register(Post)
class PostAdmin(ModelAdmin):
    pass


@admin.register(Like)
class LikeAdmin(ModelAdmin):
    pass


@admin.register(UserActivity)
class UserActivityAdmin(ModelAdmin):
    pass
