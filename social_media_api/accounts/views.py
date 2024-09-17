from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.views.generic import CreateView
# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    sucess_url = reverse_lazy('login')
    template_name = 'templates/signup.html'

class Profile(APIView):
    authentication_classes = [TokenAuthentication] # this is the implementation of token authentication
    permission_classes = [IsAuthenticated]

    def get(self ,request):
        return f"Welcome you are an authenticated user."


