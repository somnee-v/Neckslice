from django.urls import path , include
from . import views


# 22.11.06 최신욱 추가.

urlpatterns = [
    path('', views.movie_list),                           # 영화 전체 리스트
    path('<int:movie_pk>/',views.movie_detail),        # 영화 디테일 페이지
    path('average/', views.vote_average),               # 영화 평점 7점 이상 리스트
    path('genre/<genre_name>/',views.genre_list),         # 영화 장르 별 검색.                                                   

]
