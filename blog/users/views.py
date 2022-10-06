from rest_framework import generics, mixins
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from users.serializers import UserSignUpSerializer, UserDetailSerializer


class SignUpView(CreateAPIView):
    serializer_class = UserSignUpSerializer


class UserDetail(mixins.RetrieveModelMixin,
                 generics.GenericAPIView):

    queryset = User.objects.all().select_related('extendeduser')
    serializer_class = UserDetailSerializer
    permission_classes = []

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
