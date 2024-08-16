from django.urls import path
from .views import LibraryDetailView ,lists_books

urlpatterns = [
    path("books/", lists_books,name='list_books'),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name='library_list')
]