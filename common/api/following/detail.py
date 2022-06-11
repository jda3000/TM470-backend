from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from rest_framework.views import APIView

from common.models.following import Following

from common.serailizers.following import FollowingListSerializer, FollowingCreateSerializer


class FollowingDetail(APIView):

    def get(self, request):
        try:
            following_ob = Following.objects.filter(user=request.user).get(id=request.GET.get('id'))
        except ObjectDoesNotExist:
            return Response('Following detail not found', status=HTTP_400_BAD_REQUEST)
        serializer = FollowingListSerializer(following_ob, many=False)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request):
        serializer = FollowingCreateSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save(user=request.user)
            except IntegrityError:
                return Response('You are already following this user', status=HTTP_400_BAD_REQUEST)
            return Response(status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            Following.objects.filter(user=request.user).get(id=request.GET.get('id')).delete()
        except ObjectDoesNotExist:
            return Response('Following detail not found', status=HTTP_400_BAD_REQUEST)
        return Response(status=HTTP_200_OK)