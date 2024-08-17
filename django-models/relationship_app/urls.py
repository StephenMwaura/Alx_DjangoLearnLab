from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView 
from .views import lists_books , LibraryDetailView, SignUpView

urlpatterns = [
    path("books/", lists_books,name='list_books'),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name='library_list'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),

    path('register/', SignUpView.as_view(), name='register'),
]