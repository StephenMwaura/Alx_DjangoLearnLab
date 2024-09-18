from django.urls import path
from django.contrib.auth.views import LoginView
from .views import RegisterView , LoginView ,ProfileView

urlpatterns = [
    path('login/', RegisterView.as_view(), name='register'),
    path('register/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),

]