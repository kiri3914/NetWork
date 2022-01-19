from rest_framework.routers import DefaultRouter
from .views import CreatePostView, LikePostView, ListPostView

router = DefaultRouter()

router.register('create_post', CreatePostView, basename='create_post')
router.register('like_post', LikePostView, basename='like_post')
router.register('list_post', ListPostView, basename='list_post')

urlpatterns = router.urls
