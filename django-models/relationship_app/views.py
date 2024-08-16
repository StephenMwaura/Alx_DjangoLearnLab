from typing import Any
from django.shortcuts import render
from .models import Book , Library
from django.views.generic.detail import DetailView

# Create your views here.
def lists_books(request):
    return render(request ,'relationship_app/list_books.html', Book.objects.all() )
class display(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html', 'from .models import Library'

def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs) 
    context['books'] = self.objects.books.all()
    return context




        
    
 



