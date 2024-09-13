from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.forms import UserCreationForm
from .forms import  Profile_form
from django.views import View
from .forms import CustomUserCreationForm
from django.views.generic import ListView, CreateView,DetailView,UpdateView,DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
# Create your views here.
def home_view(request):
    return render(request, 'blog/home.html')

class Register(View):
   def get(self , request):
      form = UserCreationForm
      return render(request , 'register.html', {'form':form})
   def post(self , request):
      form = UserCreationForm
      if form.is_valid():
         form.save()
         return redirect('login')
      return render(request , 'register.html', {'form':form})
@login_required # authentication
def profile_view(request):
    if request.method == "POST":
        form = Profile_form(request.POST ,  instance=request.user)
        if form.is_valid():
         form.save()
         return render('profile')
    else:
       form = Profile_form(instance=request.user)

    return render(request , 'blog/profile.html', {'form':form})
    


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('blog:login')
    template_name = 'blog/signup.html'


class PostListView(ListView):
   model = Post 
   template_name = 'post_list.html'
   context_object_name = 'posts'

class PostDetailView(DetailView):
   model = Post
   template_name = 'blog/post.detail.html'

class PostCreateView(LoginRequiredMixin,CreateView):
   model = Post
   fields = ['title' , 'content']
   template_name = 'blog/post.create.html'
   success_url = reverse_lazy('posts')

   
   def form_valid(self ,form):
      form.instance.author = self.request.user
      return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView): # A class based view for updating a specific book.
   model = Post
   fields = ['title' , 'content'] # specifies the fields to be edited.
   template_name = 'blog/post.update.html'
   success_url = reverse_lazy('posts') # url to redirect after a succesful update

   
   def test_func(self):
      post = self.get_object()
      return self.request.user == post.author
  
class PostDeleteView(DeleteView):
   model = Post
   template_name = 'blog/post.delete.html'

   def test_func(self):
      post = self.get_object()
      return self.request.user == post.author