from rest_framework import serializers

from beats.models import Beat


class BeatDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beat
        fields = '__all__'


class BeatSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beat
        geo_field = 'route'
        fields = (
            'description',
            'route',
        )
