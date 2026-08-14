from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.PostListCreateAPIView.as_view()),
    path('<int:id>/', views.PostDetailAPIView.as_view()),
    path('<int:id>/comments/', views.CommentListCreateAPIView.as_view()),
]