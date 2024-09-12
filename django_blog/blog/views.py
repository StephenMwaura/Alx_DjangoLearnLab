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
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'blog/signup.html'



