from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

from user.serializers.forgotten_password import ForgottenPasswordSerializer


from django.core.mail import send_mail

from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

User = get_user_model()


class ForgottenPassword(APIView):
    permission_classes = []

    def post(self, request):
        serializer = ForgottenPasswordSerializer(data=request.data)
        if serializer.is_valid():
            try:
                # find user
                user = User.objects.get(email=serializer.validated_data['email'])

                subject = "Password Reset Requested"
                email_template_name = "password/reset_email.txt"
                context = {
                    'domain': '127.0.0.1:8000',
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user),
                    'protocol': 'http',
                }
                email = render_to_string(email_template_name, context)
                send_mail(subject, email, 'admin@example.com', [user.email], fail_silently=False)
            except ObjectDoesNotExist:
                # user not found
                pass

            return Response('Password reset initiated', status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)