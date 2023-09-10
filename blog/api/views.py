
from rest_framework import generics


from django.contrib.auth.models import User
from .models import Post, Comment, Category
from . import serializers
from .permissions import IsOwnerOrReadOnly
from rest_framework import permissions

# User List API View
class UserList(generics.ListAPIView):
    '''
    API view to retrieve the list of all users.
    queryset - fetching all user objects from the database
    serializer_class - using the UserSerializer to serialize the queryset
    '''
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    '''
    API view to retrieve details of a single user.
    '''
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class PostList(generics.ListCreateAPIView):
    '''
    API view to retrieve the list of all posts or create a new post.
    permission_classes - setting permissions
    serializer.save - saving the owner while creating a new post
    '''
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# Post Retrieve, Update, and Destroy API View
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    API view to retrieve, update, or delete a single post.
    '''
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class CommentList(generics.ListCreateAPIView):
    '''
    API view to retrieve the list of all comments or create a new comment.
    '''
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    API view to retrieve, update, or delete a single comment.
    '''
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class CategoriesList(generics.ListCreateAPIView):
    '''
    API view to retrieve the list of all categories or create a new category.
    '''
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CategoriesDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    API view to retrieve, update, or delete a single category.
    '''
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
