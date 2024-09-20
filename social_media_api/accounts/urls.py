from django.urls import path

from .views import RegisterView , LoginView ,ProfileView , FollowView , UnfollowView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('follow/<str:username>/', FollowView.as_view(), name='follow_user'),
    path('unfollow/<str:username>/', UnfollowView.as_view(), name='unfollow_user'),
]