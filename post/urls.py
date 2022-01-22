from rest_framework.routers import DefaultRouter
from .views import ListLikeViewSet, ListPostViewSet, ListUnLikeViewSet

router = DefaultRouter()

router.register('list_post', ListPostViewSet)
router.register('list_like', ListLikeViewSet)
router.register('list_unlike', ListUnLikeViewSet)

urlpatterns = router.urls


# router.register('create_post', CreatePostView)
# router.register('list_post', ListPostView)
#
# router.register('create_like', CreateLikeView)
# router.register('list_like', ListLikeView)

# router.register('like_post', UnLikePostView)
# router.register('list_post', ListPostView, basename='list_post')

# urlpatterns = router.urls

# from django.urls import path
# from .views import CreatePostView, ListPostView, CreateLikeView, ListLikeView
# from rest_framework.permissions import IsAuthenticated
#
# urlpatterns = [
#     path('create_post', CreatePostView.as_view({'post': 'create'})),
#     path('list_post', ListPostView.as_view({'get': 'list'})),
#
#     path('like_post', ListLikeView.as_view({'post': 'create'})),
#     path('list_post', CreateLikeView.as_view({'get': 'list'})),
# ]
