from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.core.exceptions import ValidationError
# from django.forms import Form

# class CustomUserCreationForm(UserCreationForm):
from .models import CustomUser
from .models import CustomUser

class Profile_form(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [ 'username', 'email', 'photo', 'bio']
