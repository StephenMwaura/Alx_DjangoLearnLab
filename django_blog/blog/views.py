from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home_view(request):
    return render(request, 'blog/home.html')
@login_required
def profile_view(request):
    user = request.user
    return render(request , 'blog/profile.html', {'user':user})
    


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'blog/signup.html'

    # def form_valid(request):

    #  if request == "POST":
    #     form = UserCreationForm()
    #     if form.is_valid():
    #         form.save()   
    #         return (request, 'Account created successfully')   
    #     else:
    #         form = UserCreationForm() 
    #         context = {'form':form} 
    #         return render(request,'register.html' , context)


