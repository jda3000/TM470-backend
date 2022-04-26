from rest_framework import serializers

from beats.models import Beat
from common.serailizers.like import LikeDetailSerializer
from common.serailizers.user import UserBasicSerializer
from common.serailizers.files import FileSerializer
from common.serailizers.comment import CommentListSerializer


class BeatDetailSerializer(serializers.ModelSerializer):
    comments = CommentListSerializer(source='comment_set', many=True)
    likes = LikeDetailSerializer(source='like_set', many=True)
    files = FileSerializer(source='file_set', many=True)
    user = UserBasicSerializer()

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
            'start_time',
            'end_time',
            'litter_collected_amount',
        )
