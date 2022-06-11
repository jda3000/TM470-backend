from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from beats.models import Beat

from beats.serailizers.list import BeatListSerializer, BeatListLoadSerailizer
from common.models.following import Following


class BeatsPublicList(APIView):
    """ all public routes """

    def get(self, request):
        # init
        number_of_results = 4
        # load serializer to manage parameters
        load_serializer = BeatListLoadSerailizer(data=request.GET)
        if load_serializer.is_valid():
            # get first N of object or skip the first N
            exclude_first = load_serializer.validated_data['exclude_first']

            beats = Beat.objects.exclude(private=True).order_by('-date_created')
            if exclude_first:
                beats = beats[exclude_first:exclude_first + number_of_results]
            else:
                beats = beats[:number_of_results]

            serializer = BeatListSerializer(beats, many=True)

            return Response(serializer.data, status=HTTP_200_OK)
        return Response(load_serializer.errors, status=HTTP_400_BAD_REQUEST)


class BeatsFollowingList(APIView):
    """ all public that user is following routes """

    def get(self, request):
        # init
        number_of_results = 4
        # load serializer to manage parameters
        load_serializer = BeatListLoadSerailizer(data=request.GET)
        if load_serializer.is_valid():
            # get first N of object or skip the first N
            exclude_first = load_serializer.validated_data['exclude_first']

            followed_users = list(Following.objects.filter(user=request.user).values_list('recipient_id', flat=True))
            followed_users.append(request.user.id)
            beats = Beat.objects.filter(user_id__in=followed_users).exclude(private=True).order_by('-date_created')
            if exclude_first:
                beats = beats[exclude_first:exclude_first + number_of_results]
            else:
                beats = beats[:number_of_results]

            serializer = BeatListSerializer(beats, many=True)

            return Response(serializer.data, status=HTTP_200_OK)
        return Response(load_serializer.errors, status=HTTP_400_BAD_REQUEST)


class BeatsUserList(APIView):
    """ a users routes """

    def get(self, request):
        # init
        number_of_results = 4
        # load serializer to manage parameters
        load_serializer = BeatListLoadSerailizer(data=request.GET)
        if load_serializer.is_valid():
            # get first N of object or skip the first N
            exclude_first = load_serializer.validated_data['exclude_first']
            if exclude_first:
                beats = Beat.objects.filter(user=request.user).order_by('-date_created')[exclude_first:exclude_first + number_of_results]
            else:
                beats = Beat.objects.filter(user=request.user).order_by('-date_created')[:number_of_results]

            serializer = BeatListSerializer(beats, many=True)

            return Response(serializer.data, status=HTTP_200_OK)
        return Response(load_serializer.errors, status=HTTP_400_BAD_REQUEST)
