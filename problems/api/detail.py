from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from problems.models import Problem

from problems.serializers.detail import ProblemSaveSerializer, ProblemDetailSerializer


class ProblemDetail(APIView):

    def get(self, request):
        try:
            problem_ob = Problem.objects.get(id=request.GET.get('id'))
        except ObjectDoesNotExist:
            return Response(status=HTTP_400_BAD_REQUEST)

        serializer = ProblemDetailSerializer(instance=problem_ob)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request):
        serializer = ProblemSaveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            Problem.objects.filter(user=request.user).get(id=request.GET.get('id')).delete()
        except ObjectDoesNotExist:
            return Response('Problem not found', status=HTTP_400_BAD_REQUEST)
        return Response(status=HTTP_200_OK)

    def patch(self, request):
        try:
            problem_ob = Problem.objects.filter(user=request.user).get(id=request.GET.get('id'))
        except ObjectDoesNotExist:
            return Response('Problem not found', status=HTTP_400_BAD_REQUEST)

        serializer = ProblemDetailSerializer(instance=problem_ob, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
