from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework.views import APIView
from django.views.generic import CreateView
from .models import CustomUser
from .serializers import RegisterSerializer ,  CustomUserSerializer
from rest_framework.authtoken.models import Token

from rest_framework.response import Response
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import status
# Create your views here.
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    
    def post(self , request):
            serializer =self.get_serializer(data=request.data)
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
        serializer = self.get_serializer(self.get_object)
        return Response(serializer.data ,status=status.HTTP_200_OK)
class LoginView(ObtainAuthToken):
     def post(self,request, *args, **kwargs):
          response = super(LoginView, self).post(request, *args, **kwargs)
          token = Token.objects.get(key=response.data['token'])
          return Response({'token': token.key}, status=status.HTTP_200_OK)