from rest_framework import serializers, validators
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSignUpSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    username = serializers.CharField(validators=[validators.UniqueValidator(User.objects.all())])

    def validate(self, attrs):
        password = attrs["password"]
        password2 = attrs["password2"]

        if password != password2:
            raise serializers.ValidationError("enter the correct password")
        return attrs

    def create(self, validated_data):

        username = validated_data["username"]
        password = validated_data["password"]
        user = User.objects.create(username=username)
        user.set_password(password)
        user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }
