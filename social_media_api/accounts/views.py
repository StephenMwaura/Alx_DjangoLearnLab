from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.views.generic import CreateView
from .models import CustomUser
from .serializers import RegisterSerializer ,  CustomUserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
# Create your views here.
class RegisterView(generics.CreateAPIView):
        def post(self , request):
             serializer = RegisterSerializer(data=request.data)
             if serializer.is_valid():
                  user = serializer.save()
                  token , created = Token.objects.get_or_create(user=user)
                  return Response({
                       "user": serializer.data,
                       "token":token.key
                  },status=status.HTTP_201_CREATED)
             return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

# allows users to retrieve and update their profile
class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def get(self ,request):
        return f"Welcome you are an authenticated user."

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username , password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'Invalid credentilas'}, status=status.HTTP_400_BAD_REQUEST)

        
