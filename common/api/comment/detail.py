from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from beats.models.beat import Beat
from common.models.comment import Comment
from common.serailizers.comment import CommentSaveSerializer, CommentListSerializer


class CommentList(APIView):

    def get(self, request):
        print(request.GET)
        try:
            beat = Beat.objects.get(id=request.GET.get('beat'))
        except ObjectDoesNotExist:
            return Response('beat does not exist', status=HTTP_400_BAD_REQUEST)

        comments = Comment.objects.filter(beat_id=beat.id).order_by('-date_created')
        serializer = CommentListSerializer(comments, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


class CommentDetail(APIView):

    def post(self, request):
        serializer = CommentSaveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
