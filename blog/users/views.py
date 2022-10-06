from rest_framework import generics, mixins
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from users.serializers import UserSignUpSerializer, UserActivitySerializer


class SignUpView(CreateAPIView):
    serializer_class = UserSignUpSerializer


class UserDetail(mixins.RetrieveModelMixin,
                 generics.GenericAPIView):

    queryset = User.objects.all()
    serializer_class = UserActivitySerializer
    permission_classes = []
    lookup_field = "user_id"
