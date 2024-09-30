from typing import Any
from django.shortcuts import render
from .models import Book , Library
from django.views.generic import DetailView , CreateView 
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView , LogoutView 
from django.contrib.auth import login

from django.urls import path
# Create your views here.
def lists_books(request): # this is a function based view
    books = Book.objects.all() # retrieves all the books
    context = {'lists_all_books':books}
    return render(request ,'list_books.html', context )
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
    
    def get_context_data(self, **kwargs):
     context = super().get_context_data(**kwargs) 
     context['books'] = self.objects.books.all()
     return context


class SignUpView(CreateView): #inherits from the django inbuilt createview form
    form_class = UserCreationForm
    success_url = reverse_lazy('login') # after a successful application the user is redirected to the next page which is 'login'
    template_name = 'register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)







        
    
 



