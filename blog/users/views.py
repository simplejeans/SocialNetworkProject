from rest_framework import generics, mixins
from rest_framework.generics import CreateAPIView

from users.models import UserActivity
from users.serializers import UserSignUpSerializer, UserActivitySerializer


class SignUpView(CreateAPIView):
    serializer_class = UserSignUpSerializer


class UserActivityView(mixins.RetrieveModelMixin, generics.GenericAPIView):

    queryset = UserActivity.objects.all()
    serializer_class = UserActivitySerializer
    permission_classes = []
    lookup_field = "user_id"

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
