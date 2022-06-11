from django.contrib.auth import get_user_model

from rest_framework import serializers

User = get_user_model()


class UserNameBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
        )

class UserFollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'image_thumb',
        )


class UserBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'image_thumb',
        )