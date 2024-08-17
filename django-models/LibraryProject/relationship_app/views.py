from typing import Any
from django.shortcuts import render
from .models import Book , Library
from django.views.generic.detail import DetailView , CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView , LogoutView 
from django.contrib.auth import login

from django.urls import path
# Create your views here.
def lists_books(request):
    books = Book.objects.all()
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


class SignUpView(CreateView):
    form_class = UserCreationForm
    sucess_url = reverse_lazy('login')
    template_name = 'register.html'

urlpatterns = [
    path('login/', LoginView.as_view(template_name = 'login.html'), name='login'),
    path('logout/',LogoutView.as_view(), name = 'logout.html')
]





        
    
 



