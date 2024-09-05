from django.urls import path, include
from .views import BookListView , BookCreateView,BookUpdateView,BookDetailView,BookDeleteView

from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),           # List all books
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),  # Get details of a single book
    path('books/create/', BookCreateView.as_view(), name='book-create'),    # Create a new book
    path('books/update/', BookUpdateView.as_view(), name='book-update'),  # Update an existing book
    path('books/delete/', BookDeleteView.as_view(), name='book-delete'),  # Delete a book
]