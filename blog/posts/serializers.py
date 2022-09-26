from rest_framework import serializers

from posts.models import Post, UserPostRelation


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


class UserPostRelationSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserPostRelation
        fields = ('post', 'like', 'unlike')



