from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.PostListCreateAPIView.as_view()),
    path('<int:pk>/', views.PostDetailAPIView.as_view()),
    path('<int:pk>/comments/', views.CommentListCreateAPIView.as_view()),
]