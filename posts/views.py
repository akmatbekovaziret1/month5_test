from django.contrib.auth.models import User
from .models import Post, Comment
from .serializers import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.db.models import Q
from . permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404

class PostListCreateAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PostListSerializer
        return PostSerializer
    
    def perform_create(self, serializer):
        serializer.save(author = self.request.user) # to make author 
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            # authenticated users can see published posts and their drafts
            return Post.objects.filter(
                Q(is_published = True) | Q(author = self.request.user)
            )
        
        return Post.objects.filter(is_published = True)
    
class PostDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # We add new parameter, so only owner of the post can modify it
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Post.objects.filter(
                Q(is_published = True) | Q(author = self.request.user)
            )
        
        return Post.objects.filter(is_published = True)

class CommentListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CommentListSerializer
        return CommentSerializer
    
    def get_queryset(self):
        post_id = self.kwargs['pk']
        if self.request.user.is_authenticated:
            # authenticated users can also see their drafts
            return Comment.objects.filter(
                post_id = post_id
                ).filter(
                    Q(is_approved = True) | Q(author = self.request.user)
                )
        return Comment.objects.filter(post_id=post_id, is_approved = True)

        
    def perform_create(self, serializer):
        post_id = self.kwargs['pk']
        # to return proper answer instead of exception
        post = get_object_or_404(Post, id=post_id, is_published = True)
        serializer.save(author = self.request.user, post = post)
        
class CommentDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = CommentSerializer
    lookup_url_kwarg = 'comment_pk'
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Comment.objects.filter(
                Q(is_approved = True) | Q(author = self.request.user)
            )
        
        return Comment.objects.filter(is_approved = True)
        
    
    
