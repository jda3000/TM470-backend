from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

from user.serializers.register import RegisterSerializer

User = get_user_model()


class Register(APIView):
    permission_classes = []

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            # create user
            user = serializer.save()

            # return jwt access codes
            tokens = RefreshToken.for_user(user)
            tokens = {
                'access': str(tokens.access_token),
                'refresh': str(tokens)
            }
            return Response(tokens, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
