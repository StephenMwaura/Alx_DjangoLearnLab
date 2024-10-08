from django.db.models.query import QuerySet
from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.forms import UserCreationForm
from .forms import  Profile_form , CommentForm
from django.views import View
from .forms import CustomUserCreationForm
from django.views.generic import ListView, CreateView,DetailView,UpdateView,DeleteView
from .models import Post , Comment
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.db.models import Q
from taggit.models import Tag
# Create your views here.
def home_view(request): #functional based views
    return render(request, 'blog/home.html') #render used to render html templates


@login_required # authentication
def profile_view(request): # a view to handle profile updates
    if request.method == "POST":
        form = Profile_form(request.POST ,  instance=request.user)
        if form.is_valid():
         form.save()
         return redirect('base')
    else:
       form = Profile_form(instance=request.user)

    return render(request , 'blog/profile.html', {'form':form})
    


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('base')
    template_name = 'blog/signup.html'

def signup_view(request):
       if request.method == 'POST':
          form = CustomUserCreationForm(request.POST)
          if form.is_valid():
             form.save()
             return redirect('base')
          else:
           return render(request , 'signup.html', {'form':form})
       else:
          form = CustomUserCreationForm()
       return render(request , 'signup.html', {'form':form})

class PostListView(ListView):
   model = Post 
   template_name = 'post_list.html'
   context_object_name = 'posts'

class PostDetailView(DetailView):
   model = Post
   template_name = 'blog/post.detail.html'

class PostCreateView(LoginRequiredMixin,CreateView): # handles creating new blog posts and ensures user is logged in
   model = Post
   fields = ['title' , 'content'] # specifies the fields for creating a new post
   template_name = 'blog/create.html'
   success_url = reverse_lazy('posts') # redirects i.e the nextpage is the posts html

   
   def form_valid(self ,form): # this method is used to set the current logged in user as the author
      form.instance.author = self.request.user
      return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView): # A class based view for updating a specific book.
   model = Post
   fields = ['title' , 'content'] # specifies the fields to be edited.
   template_name = 'blog/post.update.html'
   success_url = reverse_lazy('posts') # url to redirect after a succesful update

   
   def test_func(self): # this method checks if the current user is the author of the post
      post = self.get_object()
      return self.request.user == post.author
  
class PostDeleteView(DeleteView):
   model = Post
   template_name = 'blog/post.delete.html'

   def test_func(self):
      post = self.get_object()
      return self.request.user == post.author
   
class CommentListView(ListView):
   model = Comment
   template_name = 'blog/comment_list.html'
   context_object_name = 'comments'

   def get_queryset(self):
      post_id = self.kwargs['post_id']
      return Comment.objects.filter(post__id=post_id).order_by('-created_at')


class CommentCreateView(CreateView, LoginRequiredMixin):
   model = Comment
   form_class =CommentForm
   template_name = 'blog/comment_create.html'
   success_url = reverse_lazy('posts')

   def form_valid(self , form):
      form.instance.author = self.request.user # the comment user is the one who is logged in since he is the one who has called the instance
      form.instance.post_id = self.kwargs['post_id'] # set the related post based on the url
      return super().form_valid(form)

class CommentUpdateView(UpdateView, UserPassesTestMixin):
   model = Comment
   fields = ['content']
   template_name = 'blog/comment_update.html'
   success_url = reverse_lazy('posts')

   def test_func(self):
      comment = self.get_object()
      return self.request.user == comment.author
 

class CommentDeleteView(DeleteView, UserPassesTestMixin): # userpasses testmixin ensures that only the comment author can delete it.
   model = Comment
   fields = ['content']
   template_name = 'blog/comment_delete.html'
   success_url = reverse_lazy('posts')

   def test_func(self): # checks that only the author of the comment can delete
      comment = self.get_object()
      return self.request.user == comment.author
 
         
def view_search(request): # the q is used for complex queries
   query = request.GET.get('q')
   if query:
      posts = Post.objects.filter(
         Q(title__icontains=query), # filters posts where the queries is  found in the title
         Q(content__icontains= query), # filters posts where the queries is found in the content the icontains is used to deal with case sensitive
         Q(tags__name__icontains=query) # filters posts where the tag name contains the search query

      ).disntict() # enures the results returned are unique
   else:
      posts = Post.objects.none() # if no query is provided the search returns an empty result set
   return render(request, 'blog/results.html', {'posts':posts, 'query':query})

class PostByTagListView(ListView): # used to list posts based on a tag
   model = Post
   template_name = 'blog/posts_tag.html'
   context_object_name = 'posts'

   def get_queryset(self):
      tag_slug = self.kwargs['tag_slug'] # retrieves the tag_slug from the url parameter
      tag = Tag.objects.get(slug=tag_slug) # uses the slug to retrieve the corresponding Tag from the database
      return Post.objects.filter(tags=tag) # filters posts that are associated with the retrieved tag
   
   def get_context_data(self, **kwargs):
      context = super().get_context_date(**kwargs)
      context['tag'] = Tag.objects.get(slug=self.kwargs['tag_slug'])
      return context
class TagListView(ListView):
   model = Tag
   template_name = 'blog/tag_list.html'
   context_object_name = 'tags'
  