from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from django.contrib.gis.measure import D
from django.contrib.gis.geos import GEOSGeometry

from beats.models import Beat

from beats.serailizers.list import BeatListSerializer, BeatMapLoadSerializer


class BeatsPublicMap(APIView):
    """ public routes from co-ordinates """

    def get(self, request):
        serializer = BeatMapLoadSerializer(data=request.GET)

        if serializer.is_valid():
            point = GEOSGeometry(serializer.validated_data['coordinates'])
            # point = serializer.validated_data['coordinates']
            # latitude_delta = serializer.validated_data['latitude_delta']
            # longitude_delta = serializer.validated_data['longitude_delta']

            beats = Beat.objects.filter(private=False).filter(start_point__distance_lte=(point, D(mi=2)))
            serializer = BeatListSerializer(beats, many=True)
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
