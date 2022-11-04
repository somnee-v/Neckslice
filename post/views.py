from django.shortcuts import render
from post.models import Comment
from post.serializers import CommentSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import serializers
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
    
class CommentView(APIView):
    def get(self, request):
        post = Comment.objects.all()
        serializer = CommentSerializer(post, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializers = CommentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors) 
    
        
    pass

class PostDetailView(ListAPIView):
    def get(self, request, post_id):
        pass

