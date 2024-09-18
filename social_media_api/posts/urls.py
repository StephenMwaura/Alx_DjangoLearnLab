from .views import PostCreateApiView ,PostDeleteView,PostListView,PostUpdateView ,CommentCreateView, CommentUpdateView,CommentDeleteView,CommentListView
from django.urls import path,include
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'Post','Comment', PostCreateApiView ,PostDeleteView,PostListView,PostUpdateView ,CommentCreateView, CommentUpdateView,CommentDeleteView,CommentListView)
# urlpatterns = [
#     path('posts/' , include(router.urls))
# ]
urlpatterns = [
    path('api/posts/create/', PostCreateApiView.as_view(), name='create-post'),
    path('api/posts/',PostListView.as_view(), name='post_list'),
    path('api/posts<int:pk>/update/',PostUpdateView.as_view(), name='post_update'),
    path('api/posts<int:pk>/delete/', PostDeleteView.as_view(), name='delete-view'),
    path('api/comments/create/', CommentCreateView.as_view(), name='comment-create'),
    path('api/comments/', CommentListView.as_view(), name='comment-list'),
    path('api/comments<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('api/comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

]