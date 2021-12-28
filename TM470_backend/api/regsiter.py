from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.contrib.auth.forms import UserCreationForm


class Register(APIView):
    permission_classes = []

    def post(self, request):
        form = UserCreationForm(data=request.data)
        if form.is_valid():
            user = form.save()
            tokens = RefreshToken.for_user(user)
            tokens = {
                'access': str(tokens.access_token),
                'refresh': str(tokens)
            }
            return Response(tokens, status=HTTP_200_OK)
        return Response(form.errors, status=HTTP_400_BAD_REQUEST)
