from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.http import HttpResonse
# Create your views here.
from .models import Book
book1 = Book.objects.create(title = "Inheritance", author = "Kasoo", publication_year = 2010)
@permission_required('bookshelf.can_create', raise_exception=True) # permission required to edit the model instance
def edit_view(request): # function to edit the view
    return HttpResonse ("Edit view accessed")

