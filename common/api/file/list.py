from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from beats.models import Beat

from beats.serailizers.list import BeatListSerializer, BeatListLoadSerailizer


class BeatsList(APIView):

    def get(self, request):
        # init
        number_of_results = 4
        # load serializer to manage paramaters
        load_serializer = BeatListLoadSerailizer(data=request.GET)
        if load_serializer.is_valid():
            # get first N of object or skip the first N
            exclude_first = load_serializer.validated_data['exclude_first']
            if exclude_first:
                beats = Beat.objects.all().order_by(
                    '-date')[exclude_first:exclude_first + number_of_results]
            else:
                beats = Beat.objects.all().order_by(
                    '-date')[:number_of_results]
            serializer = BeatListSerializer(beats, many=True)

            return Response(serializer.data, status=HTTP_200_OK)
        return Response(load_serializer.errors, status=HTTP_400_BAD_REQUEST)
