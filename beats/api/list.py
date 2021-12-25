from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_403_FORBIDDEN
from rest_framework.views import APIView

from beats.models import Beat

from beats.serailizers.list import BeatListSerializer

class BeatsList(APIView):
    permission_classes = []

    def get(self, request):

        beats = Beat.objects.all()
        serializer = BeatListSerailizer(beats)
        return Response(serializer.data, status=HTTP_200_OK)