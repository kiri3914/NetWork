from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .models import Post


class ListPostView(ModelViewSet):
    http_method_names = ['get', 'head']
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny, ]


class CreatePostView(ModelViewSet):
    http_method_names = ['post', 'patch']
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAdminUser | permissions.IsAuthenticated]


class LikePostView(ModelViewSet):
    http_method_names = ['post', 'patch']
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAdminUser | permissions.IsAuthenticated]