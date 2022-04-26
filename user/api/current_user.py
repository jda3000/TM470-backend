from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView


from user.serializers.current_user import CurrentUserSerializer


class CurrentUser(APIView):

    def get(self, request):
        serializer = CurrentUserSerializer(instance=request.user)
        return Response(serializer.data, status=HTTP_200_OK)