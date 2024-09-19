from .views import CommentViewSet , PostViewset
from django.urls import path,include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'Post',PostViewset)
router.register(r'Comment',CommentViewSet)

urlpatterns = [
    path('' , include(router.urls))
]
