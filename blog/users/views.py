from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from users.serializers import UserSignUpSerializer


@api_view(['POST',])
def registration_view(request):
    if request.method == 'POST':
        serializer = UserSignUpSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'successfully registered a new user'
            data['username'] = user.username
        else:
            data = serializer.errors
        return Response(data)
