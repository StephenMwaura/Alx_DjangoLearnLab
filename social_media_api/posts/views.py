from django.shortcuts import render
from rest_framework import generics
from .models import Post ,Comment
from .serializers import PostSerializer,CommentSerializer
from django.contrib.auth.decorators import login_required, user_passes_test
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class PostCreateApiView(generics.CreateAPIView):
        queryset = Post.objects.all()
        serializer_class = PostSerializer
        permission_classes = [IsAuthenticated]
       

        
        def perform_create(self, serializer):
           serializer.save(author=self.request.user)

class PostListView(generics.ListAPIView):
        queryset = Post.objects.all()
        serializer_class = PostSerializer
       
class PostUpdateView(generics.UpdateAPIView):
        queryset = Post.objects.all()
        serializer_class = PostSerializer
        permission_classes = [IsAuthenticated]

class PostDeleteView(generics.DestroyAPIView):
        queryset = Post.objects.all()
        serializer_class = PostSerializer
        permission_classes = [IsAuthenticated]

class CommentCreateView(generics.CreateAPIView):
    quryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
class CommentListView(generics.ListAPIView):
        quryset = Comment.objects.all()
        serializer_class = CommentSerializer
        filter_backends = [DjangoFilterBackend, filters.OrderingFilter,filters.SearchFilter ]
        filterset_fields = [ 'title' , 'content', ] # allows filtering based on title and content
        search_fields = ['title' , 'content'] # allows searching by title and content

    
class CommentUpdateView(generics.UpdateAPIView):
    quryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)
    
class CommentDeleteView(generics.DestroyAPIView):
        quryset = Comment.objects.all()
        serializer_class = CommentSerializer
    
