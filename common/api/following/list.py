import pprint

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from common.models.following import Following

from common.serailizers.following import FollowingListSerializer


class FollowingList(APIView):

    def get(self, request):
        following_obs = Following.objects.filter(user=request.user)
        serializer = FollowingListSerializer(following_obs, many=True)
        pprint.pprint(serializer.data)
        return Response(serializer.data, status=HTTP_200_OK)
