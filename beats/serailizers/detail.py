from django.db.models import Q

from rest_framework import serializers

from beats.models import Beat
from common.models.following import Following

from common.serailizers.like import LikeDetailSerializer
from common.serailizers.user import UserBasicSerializer
from common.serailizers.files import FileSerializer
from common.serailizers.comment import CommentListSerializer
from common.serailizers.following import FollowingBeatDetailSerializer


class BeatDetailSerializer(serializers.ModelSerializer):
    comments = CommentListSerializer(source='comment_set', many=True)
    likes = LikeDetailSerializer(source='like_set', many=True)
    files = FileSerializer(source='file_set', many=True)
    user = UserBasicSerializer()
    following = serializers.SerializerMethodField()

    class Meta:
        model = Beat
        fields = '__all__'

    def get_following(self, instance):
        try:
            user = self.context.get('user')
            following = Following.objects.get(Q(user=user) & Q(recipient=instance.user))
            serializer = FollowingBeatDetailSerializer(following)
            return serializer.data
        except Exception:
            return None


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
            'private',
        )
