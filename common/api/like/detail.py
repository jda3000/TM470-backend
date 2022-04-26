from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from common.models.like import Like
from beats.models.beat import Beat
from common.serailizers.like import LikeSaveSerializer, LikeDetailSerializer


class ListList(APIView):

    def get(self, request):
        try:
            beat = Beat.objects.get(id=request.GET.get('beat'))
        except ObjectDoesNotExist:
            return Response('Beat does not exist', status=HTTP_400_BAD_REQUEST)
        likes = Like.objects.filter(beat_id=beat.id)
        serializer = LikeDetailSerializer(likes, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


class LikeDetail(APIView):

    def post(self, request):
        serializer = LikeSaveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            Like.objects.filter(user=request.user).get(id=request.GET.get('id')).delete()
        except ObjectDoesNotExist:
            return Response('Like not found', status=HTTP_400_BAD_REQUEST)
        return Response(status=HTTP_200_OK)
