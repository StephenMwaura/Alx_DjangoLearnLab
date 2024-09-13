from django.urls import path
from .views import SignUpView
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView , LogoutView
from django.contrib.auth import views

urlpatterns = [
    path('home', TemplateView.as_view(template_name = "blog/home.html") , name='home'),
    path("register/", SignUpView.as_view(), name="register"),
    path('login/',views.LoginView.as_view(template_name = 'blog/login.html')),
    path('profile/', TemplateView.as_view(template_name = 'blog/profile.html'), name="profile"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('base/', TemplateView.as_view(template_name = 'blog/base.html'), name='base' )
]