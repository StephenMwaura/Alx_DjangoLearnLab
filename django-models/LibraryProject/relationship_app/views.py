from typing import Any
from django.shortcuts import render
from .models import Book , Library
from django.views.generic.detail import DetailView

# Create your views here.
def lists_all_books(request):
    books = Book.objects.all()
    context = {'lists_all_books':books}
    return render(request ,'list_books.html', context )
class LibraryListView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs) 
    context['books'] = self.objects.books.all()
    return context




        
    
 



