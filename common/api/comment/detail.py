from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from beats.models import Beat

from beats.serailizers.detail import BeatSaveSerializer, BeatDetailSerializer


class BeatDetail(APIView):

    def get(self, request):
        try:
            beat = Beat.objects.get(id=request.GET.get('id'))
        except ObjectDoesNotExist:
            return Response(status=HTTP_400_BAD_REQUEST)

        serializer = BeatDetailSerializer(instance=beat)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request):
        serializer = BeatSaveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            Beat.objects.filter(user=request.user).get(id=request.GET.get('id')).delete()
        except ObjectDoesNotExist:
            return Response('Beat not found', status=HTTP_400_BAD_REQUEST)
        return Response(status=HTTP_200_OK)
