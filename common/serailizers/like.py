from rest_framework import serializers

from common.models.like import Like

from common.serailizers.user import UserNameBasicSerializer, UserBasicSerializer


class LikeSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = (
            'user',
            'beat',
        )
        unique_together = ['user', 'beat']


class LikeDetailSerializer(serializers.ModelSerializer):
    user = UserBasicSerializer()

    class Meta:
        model = Like
        fields = (
            'id',
            'date_created',
            'user',
        )
