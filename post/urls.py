from django.urls import path, include
from post import views

urlpatterns = [
    path('comment/', views.CommentView.as_view(), name='comment_view'),
]


