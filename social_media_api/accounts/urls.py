from django.urls import path
from django.contrib.auth.views import LoginView
from .views import SignUpView , Profile

urlpatterns = [
    path('login/', LoginView.as_view(template_name='templates/login.html'), name='login'),
    path('register/', SignUpView.as_view(template_name='signup.html'), name='register'),
    path('profile/', Profile.as_view(), name='user-profile')

]