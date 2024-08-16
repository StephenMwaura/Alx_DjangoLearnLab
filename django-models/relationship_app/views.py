from typing import Any
from django.shortcuts import render
from .models import Book , Library
from django.views.generic import ListView

# Create your views here.
def lists_all_books(request):
    return render(request ,'relationship_app/list_books.html', Book.objects.all() )
class display(ListView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs) 
    context['books'] = self.objects.books.all()
    return context




        
    
 



