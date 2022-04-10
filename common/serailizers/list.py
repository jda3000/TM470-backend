from rest_framework import serializers

from beats.models import Beat


class BeatListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beat
        fields = '__all__'


class BeatListLoadSerailizer(serializers.Serializer):
    exclude_first = serializers.IntegerField(required=True)
