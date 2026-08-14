from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'id username'.split()

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only = True)
    class Meta:
        model = Post
        fields = '__all__'

class PostListSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only = True)
    class Meta:
        model = Post
        fields = 'id author title created_at'.split()

class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only = True)
    post = PostListSerializer(read_only = True)
    class Meta:
        model = Comment
        fields = '__all__'

class CommentListSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only = True)
    post = PostListSerializer(read_only = True)
    class Meta:
        model = Comment
        fields = 'id post author created_at'.split()

