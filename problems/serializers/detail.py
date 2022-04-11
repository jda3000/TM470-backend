from rest_framework import serializers

from problems.models import Problem


class ProblemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = '__all__'


class ProblemSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        geo_field = 'location'
        fields = (
            'description',
            'location',
        )
