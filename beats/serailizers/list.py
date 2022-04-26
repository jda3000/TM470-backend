from rest_framework import serializers

from beats.models import Beat

from common.serailizers.like import LikeDetailSerializer
from common.serailizers.user import UserBasicSerializer
from common.serailizers.comment import CommentListSerializer


class BeatListSerializer(serializers.ModelSerializer):
    comments = CommentListSerializer(source='comment_set', many=True)
    likes = LikeDetailSerializer(source='like_set', many=True)
    user = UserBasicSerializer()

    class Meta:
        model = Beat
        fields = '__all__'


class BeatListLoadSerailizer(serializers.Serializer):
    # excludes the first number of objects found: this is for a rolling list on client application
    exclude_first = serializers.IntegerField(required=True)
