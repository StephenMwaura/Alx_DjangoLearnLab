from typing import Any
from django.shortcuts import render
from .models import Book , Library
from django.views.generic.detail import DetailView , CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView , LogoutView
from django.urls import path


# Create your views here.
def lists_books(request):
    return render(request ,'relationship_app/list_books.html', Book.objects.all() )
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html', 'from .models import Library'

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





        
    
 



