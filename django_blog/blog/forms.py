from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser , Post

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = CustomUser
        fields = [ 'username', 'email', 'bio', 'photo']

class Profile_form(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email' , 'bio' , 'photo']

class Create_model(forms.ModelForm):
    model  = Post
    fields = [ ' title' , 'content' , 'published_date' , 'author']

class Update_model(forms.ModelForm):
    model = Post
    fields = [ 'title' , 'content']