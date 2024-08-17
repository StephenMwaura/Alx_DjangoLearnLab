from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView 
from .views import list_books 
from .views import LibraryDetailView
from .import views
from .templates.relationship_app import Admin_view
from .templates.relationship_app import librarian_view
from .templates.relationship_app import member_view
from .views import add_book, edit_book, delete_book, list_books

urlpatterns = [
    path("books/", list_books,name='list_books'),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name='library_list'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),

    path('register/', views.register.as_view(), name='register'),
    path('admin/', Admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
    path('books/add/', add_book, name='add_book'),
    path('books/edit/<int:pk/>', edit_book, name='edit_book'),
    path('books/delete/<int:pk>/', delete_book, name='delete_book'),
]