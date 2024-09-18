from .views import PostCreateApiView ,PostDeleteView,PostListView,PostUpdateView ,CommentCreateView, CommentUpdateView,CommentDeleteView,CommentListView
from django.urls import path,include
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'Post','Comment', PostCreateApiView ,PostDeleteView,PostListView,PostUpdateView ,CommentCreateView, CommentUpdateView,CommentDeleteView,CommentListView)
# urlpatterns = [
#     path('posts/' , include(router.urls))
# ]
urlpatterns = [
    path('postcreate/', PostCreateApiView.as_view(), name='create-post'),
    path('postlist/',PostListView.as_view(), name='post_list'),
    path('postupdate/',PostUpdateView.as_view(), name='post_update'),
    path('postdelete/', PostDeleteView.as_view(), name='delete-view'),
    path('commentcreate/', CommentCreateView.as_view(), name='comment-create'),
    path('commentlist/', CommentListView.as_view(), name='comment-list'),
    path('commentupdate/', CommentUpdateView.as_view(), name='comment-update'),
    path('commentdelete/', CommentDeleteView.as_view(), name='comment-delete'),

]