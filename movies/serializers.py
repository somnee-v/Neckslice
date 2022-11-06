from rest_framework import serializers
from .models import  Movie ,Genre


# 22.11.06 최신욱 추가.

#무비 id와 타이틀
class MovieTitleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('id', 'title')

# 무비 전체 API
class MovieDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = "__all__"

# 장르
class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = '__all__'
