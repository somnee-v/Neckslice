from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.db.models import Q
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from .models import Movie ,Genre
from .serializers import MovieTitleSerializer ,MovieDetailSerializer, GenreSerializer


# 22.11.06 최신욱 추가.

BASE_IMAGE_URL = 'https://image.tmdb.org/t/p/w500'
POSTER_PATH = ''

# 영화 리스트 전체
@api_view(['GET'])
def movie_list(request):
    movie_lists = get_list_or_404(Movie)
    serializer = MovieTitleSerializer(movie_lists, many=True)
    return Response(serializer.data)

# 영화 상세정보 페이지 1번 방법
@api_view(['GET'])
def movie_detail1(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer =  MovieDetailSerializer(movie)
    return Response(serializer.data)

##무비 상세정보 페이지 2번 방법
@api_view(['GET'])
def movie_detail2(request, movie_pk ):
    movie = get_object_or_404(Movie, pk=movie_pk)
    genre = movie.genres.all()
    serializer = MovieDetailSerializer(movie)
    serializer2 = GenreSerializer(genre, many=True)
    return Response([serializer.data, serializer2.data])

# 평점이 7점 이상인 영화들만 불러오기
@api_view(['GET']) 
def vote_average7(request):
    movies = Movie.objects.filter(vote_average__gte=7.0)
    serializer = MovieDetailSerializer(movies, many=True)
    return Response(serializer.data)


#장르별 리스트 출력
@api_view(['GET'])
def genre_list(request, genre_name):
    genre = get_object_or_404(Genre, name=genre_name)
    movies = Movie.objects.filter(Q(genres__id__contains=genre.pk))
    serializer = MovieDetailSerializer(movies, many=True)
    return Response(serializer.data)


