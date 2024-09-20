from .views import CommentViewSet , PostViewset , FeedView
from django.urls import path,include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'Post',PostViewset)
router.register(r'Comment',CommentViewSet)

urlpatterns = [
    path('feed/',FeedView.as_view(), name='user_feed'),
    path('' , include(router.urls))
]
