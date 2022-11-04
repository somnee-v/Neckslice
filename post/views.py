from rest_framework.generics import ListAPIView
from rest_framework import status, permissions
from rest_framework.response import Response

from rest_framework.filters import SearchFilter
#from rest_framework import django_filters
from django_filters.rest_framework import DjangoFilterBackend

from post.serializers import PostSerializer
from post.models import Post
# Create your views here.
class PostView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filter_fields = ['title']
    search_fields = ['title', 'contant']
    
    
        
    pass

class PostDetailView(ListAPIView):
    def get(self, request, post_id):
        pass