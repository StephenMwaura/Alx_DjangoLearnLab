from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm 
from .models import CustomUser , Post , Comment
from taggit.forms import TagWidget
class CustomUserCreationForm(UserCreationForm): # an extension of djangos built in creation form
    email = forms.EmailField(required=True)
    
    class Meta:
        model = CustomUser
        fields = [ 'username', 'email', 'bio', 'photo']

    def clean_name(self):
        username = self.cleaned_data.get('username')
        if len(username) < 3:
            raise forms.ValidationError("Username must be more that 5 characters.")
        return username
class Profile_form(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email' , 'bio' , 'photo']

class Create_model(forms.ModelForm):
    class Meat:
        model  = Post
        fields = [ ' title' , 'content' , 'published_date' , 'author']

class Update_model(forms.ModelForm):
    class Meta:
        model = Post
        fields = [ 'title' , 'content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        
        fields = ['content' ]

class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False , widget=TagWidget())
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']