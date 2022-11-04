from .models import Comment
from rest_framework import serializers

class CommentSerializer(serializers.ModelSerializer):
    # users = serializers.ReadOnlyField(source = 'users.email')
    class Meta:
        model = Comment
        fields = ['user','content','created_at','updated_at']

