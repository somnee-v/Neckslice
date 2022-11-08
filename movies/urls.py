from django.urls import path , include
from . import views


# 22.11.06 최신욱 추가.

urlpatterns = [
<<<<<<< HEAD
    path('', views.movie_list),                  #영화 전체 리스트
    path('1/<int:movie_pk>/', views.movie_detail1),  # 영화 디테일 페이지 방법 1
    path('/<int:movie_pk>/',views.movie_detail2),   # 영화 디테일 페이지 방법 2
    path('average7/', views.vote_average7),        # 영화 평점 7점 이상 리스트
    path('genre/<genre_name>/',views.genre_list),         # 영화 장르 별 검색.
=======
    path('', views.movie_list),                           # 영화 전체 리스트
    path('<int:movie_pk>/',views.movie_detail),        # 영화 디테일 페이지
    path('average/', views.vote_average),               # 영화 평점 7점 이상 리스트
    path('genre/<genre_name>/',views.genre_list),         # 영화 장르 별 검색. 
    path('<int:movie_pk>/comment/', views.CommentView.as_view(), name='comment_view'), # 검색
    path('comment/<int:comment_id>/', views.CommentDetailView.as_view(), name='commentdetai_view'),                                           

]
>>>>>>> 40da30f89d251c8c82460a2063cc50f6f0b35661

