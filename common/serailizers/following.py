from rest_framework import serializers

from common.models.following import Following
from common.serailizers.user import UserFollowingSerializer


class FollowingListSerializer(serializers.ModelSerializer):
    recipient = UserFollowingSerializer()

    class Meta:
        model = Following
        fields = '__all__'


class FollowingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Following
        fields = (
            'recipient',
        )


class FollowingBeatDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Following
        fields = (
            'id',
            'recipient',
        )