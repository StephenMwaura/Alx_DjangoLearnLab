from django.contrib.auth.decorators import permission_required 
from django.contrib.auth import login

from typing import Any
from django.shortcuts import render
from .models import Book 

from .models import Library
from django.views.generic.detail import DetailView , CreateView 
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView , LogoutView 
from .templates.relationship_app import Admin_view
from .templates.relationship_app import librarian_view
from .templates.relationship_app import member_view
from  django.contrib.auth.decorators import user_passes_test , permission_required 
from django.shortcuts import render, get_object_or_404,redirect



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


def is_Admin(user):
    return user.is_authenticated and user.groups.filter(name='Admin').exists()
@user_passes_test(is_Admin)
def Admin_view(request):
    return render("request , 'relationship_app/admin_view.html")


def is_Libranian(user):
    return user.is_authenticated and user.groups.filter(name='Libranian').exists()
@user_passes_test(is_Libranian)
def Librarian_view(request):
    return render("request , 'relationship_app/librarian_view.html")



def is_Member(user):
    return user.is_authenticated and user.groups.filter(name='Member').exists()
@user_passes_test(is_Member)
def member_view(request):
    return render("request , 'relationship_app/member_view.html")

@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        published_date = request.POST.get('published_date')

        if title and author and published_date:
            Book.objects.create(title=title, author=author, published_date=published_date)
            return redirect('list_books')
        

@permission_required('relationship_app.can_change_book')
def edit_book(request , pk):
    book = get_object_or_404(Book , pk=pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        published_date = request.POST.get('published_date')

        if title and author and published_date:
            Book.objects.create(title=title, author=author, published_date=published_date)
            return redirect('list_books')
        

@permission_required('relationship_app.can_delete_book')
def delete_book(request,pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
       book.delete()
       return redirect('list_books')
        
       




urlpatterns = [
    path('login/', LoginView.as_view(template_name = 'login.html'), name='login'),
    path('logout/',LogoutView.as_view(), name = 'logout'),
    path('register/',register.as_view(), name='register'),
    path('admin/', Admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
]





        
    
 



