from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from rest_framework.views import APIView

from beats.models import Beat

from beats.serailizers.detail import BeatSaveSerializer, BeatDetailSerializer


class BeatDetail(APIView):

    def get(self, request):
        try:
            beat_ob = Beat.objects.get(id=request.GET.get('id'))
        except ObjectDoesNotExist:
            return Response(status=HTTP_400_BAD_REQUEST)

        serializer = BeatDetailSerializer(instance=beat_ob)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request):
        serializer = BeatSaveSerializer(data=request.data)
        if serializer.is_valid():
            beat = serializer.save(user=request.user)
            serializer = BeatDetailSerializer(instance=beat)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            Beat.objects.filter(user=request.user).get(id=request.GET.get('id')).delete()
        except ObjectDoesNotExist:
            return Response('Beat not found', status=HTTP_400_BAD_REQUEST)
        return Response(status=HTTP_204_NO_CONTENT)

    def patch(self, request):
        try:
            beat_ob = Beat.objects.filter(user=request.user).get(id=request.data.get('id'))
        except ObjectDoesNotExist:
            return Response('Beat not found', status=HTTP_400_BAD_REQUEST)

        serializer = BeatDetailSerializer(instance=beat_ob, partial=True, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
