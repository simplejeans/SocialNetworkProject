
from rest_framework import serializers, request

from posts.models import Post, Like


class PostSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        author = self.context["request"].user
        validated_data["author"] = author
        return super().create(validated_data)


class LikesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('post', 'like')

    @staticmethod
    def make_unlike(self):
        post = Post.objects.get(likes_id=request.user.id)
        if post.exists():
            post.remove(request.user)






