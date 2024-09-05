from django.shortcuts import render
from rest_framework import generics , permissions
from .models import Book
from .seriealizers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# Create your views here.
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all() # retrieve all the books
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
class BookDetailView(generics.RetrieveAPIView ):
    queryset = Book.objects.all  # retrieving a single book by id
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all() # adding a new book
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]




class BookUpdateView(generics.UpdateAPIView): # for updating an existing book
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()# deleting an existing book
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]