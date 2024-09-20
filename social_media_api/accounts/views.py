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
     
class FollowView(APIView):
     permission_classes = [IsAuthenticated]

     def post(self, request, username):
        try:
            follow_user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
             return Response({'info':"User not found."}, status=status.HTTP_404_NOT_FOUND)
        
        if request.user == follow_user:
             return Response({'info': 'You cannot follow yourself'} ,status=status.HTTP_400_BAD_REQUEST)
        
        if request.user in follow_user.followers.all():
             return Response({"info":"You are already following this user"}, status=status.HTTP_400_BAD_REQUEST)
        
        follow_user.followers.add(request.user)
        return Response({"info":"You are now following {username}"}, status=status.HTTP_200_OK)
     

class UnfollowView(APIView):
     permission_classes = [IsAuthenticated]

     def post(user , request, username):
          try:
            follow_user = CustomUser.objects.get(username=username)
          except CustomUser.DoesNotExist:
               return Response({"info":"User not found."}, status=status.HTTP_404_NOT_FOUND)
          
          if request.user == follow_user:
               return Response({"info:You cannot unfollow yourself"})
          
          if request.user not in follow_user.followers.all():
               return Response({"info":"You are not following this {username}."}, status=status.HTTP_400_BAD_REQUEST)
          follow_user.followers.remove(request.user)
          return Response({"info":"You have unfollowed{username}."}, status=status.HTTP_200_OK)

          

        
          
     