from django.contrib import admin
from django.contrib.admin import ModelAdmin

from posts.models import Post, UserPostRelation


@admin.register(Post)
class PostAdmin(ModelAdmin):
    pass


@admin.register(UserPostRelation)
class UserPostRelationAdmin(ModelAdmin):
    pass
