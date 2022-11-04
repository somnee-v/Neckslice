from django.urls import path, include
from post import views


urlpatterns = [
    path('', views.PostView.as_view(), name='post_view'),
    path('<int:post_id>', views.PostDetailView.as_view(), name='post_detail_view'),
]
