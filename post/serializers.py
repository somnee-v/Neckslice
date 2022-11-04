
from rest_framework import serializers
from post.models import Post
from .models import Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    # users = serializers.ReadOnlyField(source = 'users.email')
    class Meta:
        model = Comment
        fields = ['user','content','created_at','updated_at']


