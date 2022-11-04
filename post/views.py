from django.shortcuts import render
from post.models import Comment
from post.serializers import CommentSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import serializers

# Create your views here.
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