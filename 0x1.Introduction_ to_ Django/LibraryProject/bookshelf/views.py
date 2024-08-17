from django.shortcuts import render

# Create your views here.
from .models import Book

book1 = Book.objects.create(title = "Inheritance", author = "Kasoo", publication_year = 2010)
