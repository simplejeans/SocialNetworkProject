from django.contrib import admin
from django.contrib.admin import ModelAdmin

from posts.models import Post, Like


@admin.register(Post)
class PostAdmin(ModelAdmin):
    pass


@admin.register(Like)
class LikeAdmin(ModelAdmin):
    pass
