from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

from .models import Post, Like, UnLike
from .serializers import LikeSerializer, UnLikeSerializer


class LikeMixins:

    @action(methods=['post'], detail=True, serializer_class=LikeSerializer)
    def set_like(self, request, *args, **kwargs):
        post = self.get_object()
        owner = request.user
        like = Likes.objects.filter(post=post, owner=owner)
        dislike = DisLikes.objects.filter(post=post, owner=owner)
        if like.exists():
            like.delete()
            post.likes -= 1
            post.save()
            return Response({'Message': "Вы убрали лайк"}, status=status.HTTP_200_OK)

        else:
            if dislike.exists():
                dislike.first().delete()
                post.dislikes -= 1

            Likes.objects.create(owner=owner, post=post)
            post.likes += 1
            post.save()
            return Response({"Message": "Вы поставили лайк"}, status=status.HTTP_201_CREATED)


class UnLikeMixins:

    @action(methods=['post'], detail=True, serializer_class=UnLikeSerializer)
    def set_dislike(self, request, *args, **kwargs):
        post = self.get_object()
        owner = request.user
        like = Likes.objects.filter(post=post, owner=owner)
        unlike = UnLikes.objects.filter(post=post, owner=owner)
        if unlike.exists():
            unlike.delete()
            post.unlikes -= 1
            post.save()
            return Response({'Message': "Вы убрали дизлайк"}, status=status.HTTP_200_OK)

        else:
            if like.exists():
                like.first().delete()
                post.likes -= 1

            UnLikes.objects.create(owner=owner, post=post)
            post.unlikes += 1
            post.save()
            return Response({"Message": "Вы поставили дизлайк"}, status=status.HTTP_201_CREATED)
