
from rest_framework import generics
from .models import Post ,Comment
from .serializers import PostSerializer,CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .permissions import IsAuthorOrReadOnly
from rest_framework import generics
from rest_framework import permissions

from rest_framework import viewsets
# Create your views here.
# the modelviewset allows implementation such as list create or retrieve
class PostViewset(viewsets.ModelViewSet): #handles all basic crud operations for the post model
        queryset = Post.objects.all()
        serializer_class = PostSerializer
        permission_classes = [IsAuthorOrReadOnly]
        filter_backends = [DjangoFilterBackend,filters.SearchFilter ]
        filterset_fields = [ 'title'] # allows filtering based on title and content
        search_fields = ['title'] # allows searching by title and content


        
        def perform_create(self, serializer):
           serializer.save(author=self.request.user)






class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes =  [IsAuthorOrReadOnly]
  
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FeedView(generics.ListAPIView): # lists all the posts of the people the user is following
     serializer_class = PostSerializer
     permission_classes = [permissions.IsAuthenticated]
     
     def get_queryset(self):
        user = self.request.user
        following_users = user.following.all() # users that the current user follows
        return Post.objects.filter(author__in=following_users).order_by('-created_at')