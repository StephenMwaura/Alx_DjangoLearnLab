from django.urls import path
from .views import SignUpView
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView , LogoutView
from django.contrib.auth import views as  auth_views
from .import views
urlpatterns = [
    path('home', TemplateView.as_view(template_name = "blog/home.html") , name='home'),
    path("register/", SignUpView.as_view(), name="register"),
    path('login/',auth_views.LoginView.as_view(template_name = 'blog/login.html'), name = 'login'),
    path('profile/', TemplateView.as_view(template_name = 'blog/profile.html'), name="profile"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('base/', TemplateView.as_view(template_name = 'blog/base.html'), name='base' ),
    path('posts/',views.PostListView.as_view(), name='posts'),
    path ('post/new/', views.PostCreateView.as_view(), name='Create'),
    path('post/update/<int:pk>/', views.PostUpdateView.as_view() ,  name="update"),
    path('post/delete/<int:pk>', views.PostDeleteView.as_view(), name='delete'),
] 
