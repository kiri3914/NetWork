from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from .mixins import LikeMixins, UnLikeMixins
from .serializers import PostSerializer, LikeSerializer, UnLikeSerializer
from .models import Post, Like, UnLike


class ListPostViewSet(LikeMixins, UnLikeMixins, ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [permissions.IsAdminUser | permissions.IsAuthenticated]


class ListLikeViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    # permission_classes = [permissions.IsAdminUser | permissions.IsAuthenticated]


class ListUnLikeViewSet(ModelViewSet):
    queryset = UnLike.objects.all()
    serializer_class = UnLikeSerializer
    # permission_classes = [permissions.IsAdminUser | permissions.IsAuthenticated]
