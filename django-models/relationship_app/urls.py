from django.urls import path
from .import views

urlpatterns = [
    path("books/", views.list_all_books,name='list_books'),
      path("library/", views.LibraryListView.as_view(), name='library_list')
]