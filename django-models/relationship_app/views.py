from django.contrib.auth import login
from typing import Any
from django.shortcuts import render
from .models import Book 
from .models import Library
from django.views.generic.detail import DetailView , CreateView 
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView , LogoutView 


from django.urls import path
# Create your views here.
def list_books(request):
    books = Book.objects.all()
    context = {'lists_all_books':books}
    return render(request ,'relationship_app/list_books.html', context )
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
    def get_context_data(self, **kwargs):
     context = super().get_context_data(**kwargs) 
     context['books'] = self.objects.books.all()
     return context


class  register(CreateView):
    form_class = UserCreationForm()
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

urlpatterns = [
    path('login/', LoginView.as_view(template_name = 'login.html'), name='login'),
    path('logout/',LogoutView.as_view(), name = 'logout'),
    path('register/',register.as_view(), name='register'),
    
]





        
    
 



