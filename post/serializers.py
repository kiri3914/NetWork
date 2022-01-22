from rest_framework import serializers
from .models import Post, Like, UnLike


class PostSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Post
        fields = [
            'id', 'title',
            'data_created', 'likes', 'unlikes',
        ]
        read_only_fields = ['data_created', 'likes', 'unlikes']


class LikeSerializer(serializers.ModelSerializer):
    post = serializers.ReadOnlyField(source='post.title')
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields = ['id', 'post', 'owner', 'data_created']
        read_only_fields = ['data_created']


class UnLikeSerializer(serializers.ModelSerializer):
    post = serializers.ReadOnlyField(source='post.title')
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = UnLike
        fields = ['id', 'post', 'owner', 'data_created']
        read_only_fields = ['data_created']
