from .views import PostCreateApiView ,PostDeleteView,PostListView,PostUpdateView ,CommentCreateView, CommentUpdateView,CommentDeleteView,CommentListView
from django.urls import path,include
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'Post','Comment', PostCreateApiView ,PostDeleteView,PostListView,PostUpdateView ,CommentCreateView, CommentUpdateView,CommentDeleteView,CommentListView)
# urlpatterns = [
#     path('posts/' , include(router.urls))
# ]
urlpatterns = [
    path('posts/create/', PostCreateApiView.as_view(), name='create-post'),
    path('posts/',PostListView.as_view(), name='post_list'),
    path('posts<int:pk>/update/',PostUpdateView.as_view(), name='post_update'),
    path('posts<int:pk>/delete/', PostDeleteView.as_view(), name='delete-view'),
    path('comments/create/', CommentCreateView.as_view(), name='comment-create'),
    path('comments/', CommentListView.as_view(), name='comment-list'),
    path('comments<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

]