from django.urls import path
from .views import SignUpView , CommentListView, CommentCreateView, CommentDeleteView, CommentUpdateView
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView , LogoutView
from django.contrib.auth import views as  auth_views
from . import views
from .views import profile_view
urlpatterns = [
    path('home', TemplateView.as_view(template_name = "blog/home.html") , name='home'),
    path("register/", SignUpView.as_view(), name="register"),
    path('login/',auth_views.LoginView.as_view(template_name = 'blog/login.html'), name = 'login'),
    path('profile/', profile_view, name="profile"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('base/', TemplateView.as_view(template_name = 'blog/base.html'), name='base' ),
    path('posts/',views.PostListView.as_view(), name='posts'),
    path ('post/new/', views.PostCreateView.as_view(), name='Create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view() ,  name="update"),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete'),
    path('posts/<int:post_id>/comments/new/',CommentCreateView.as_view(), name="comment_create"),
    path('posts/<int:pk>/comments/delete/',CommentDeleteView.as_view(), name='comment-_delete'),
    path('posts/<int:pk>/comments/edit/',CommentUpdateView.as_view(), name = 'comment_update'),
    path('posts/<int:post_id>/comments/',CommentListView.as_view(), name='comment_list'),

] 
