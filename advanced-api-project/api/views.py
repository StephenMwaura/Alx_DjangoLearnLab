from django.shortcuts import render
from rest_framework import generics , permissions
from .models import Book
from .seriealizers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django_filters import rest_framework
# Create your views here.
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all() # retrieve all the books
    serializer_class = BookSerializer # specifies the Book model instances to json
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] # ensures users can read the data without authentication
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter,filters.SearchFilter ]
    filterset_fileds = [ 'title' , 'author__name', 'publication_year'] # allows filtering based on title , author and publicatin year
    search_fields = ['title' , 'author__name'] # allows searching by title and author
    ordering_fields = [ 'title' , 'publication_year' ] # allows ordering results by title or publication_year
class BookDetailView(generics.RetrieveAPIView ):
    queryset = Book.objects.all  # retrieving a single book by id
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all() # adding a new book
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated] # allows authenticated users to add new books




class BookUpdateView(generics.UpdateAPIView): # for updating an existing book
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()# deleting an existing book
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]