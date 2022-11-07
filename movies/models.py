from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from users.models import User


# 22.11.06 최신욱 추가.

#장르
class Genre(models.Model):
    name = models.TextField()
    
    def __str__(self):
      return self.name

# Create your models here.
class Movie(models.Model):
    title = models.TextField()  # 영화제목
    original_title = models.TextField() #원 제목
    release_date = models.TextField()  # 개봉연도
    genres = models.ManyToManyField(Genre, blank=True)  # 장르
    poster_path = models.TextField()  # 포스터
    backdrop_path = models.TextField(null = True) #백그라운드 포스터
    overview = models.TextField()  # 줄거리
    adult = models.BooleanField()  # 19금
    runtime = models.IntegerField(validators=[MinValueValidator(0)]) #상영시간
    vote_average = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])  # 평점
    vote_count = models.IntegerField(validators=[MinValueValidator(0)])  # 평점 투표 수 
    popularity = models.FloatField(validators=[MinValueValidator(0)])


class Comment(models.Model): # 댓글 모델 
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True) 

    def __str__(self):
        return str(self.content)