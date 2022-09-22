from rest_framework.generics import CreateAPIView


from users.serializers import UserSignUpSerializer


class SignUpView(CreateAPIView):
    serializer_class = UserSignUpSerializer
