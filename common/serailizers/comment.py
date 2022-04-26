from rest_framework import serializers

from common.models.comment import Comment

from common.serailizers.user import UserBasicSerializer


class CommentListSerializer(serializers.ModelSerializer):
    user = UserBasicSerializer()

    class Meta:
        model = Comment
        fields = (
            'date_created',
            'post',
            'user',
            'id',
        )


class CommentSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'beat',
            'post',
        )