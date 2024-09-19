
from rest_framework import generics
from .models import Post ,Comment
from .serializers import PostSerializer,CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .permissions import IsAuthorOrReadOnly

from rest_framework import viewsets
# Create your views here.
# the modelviewset allows implementation such as list create or retrieve
class PostViewset(viewsets.ModelViewSet): #handles all basic crud operations for the post model
        queryset = Post.objects.all()
        serializer_class = PostSerializer
        permission_classes = [IsAuthorOrReadOnly]
        filter_backends = [DjangoFilterBackend,filters.SearchFilter ]
        filterset_fields = [ 'title' , 'content'] # allows filtering based on title and content
        search_fields = ['title' , 'content'] # allows searching by title and content


        
        def perform_create(self, serializer):
           serializer.save(author=self.request.user)






class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes =  [IsAuthorOrReadOnly]
  
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

