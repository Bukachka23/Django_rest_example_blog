from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Comment, Category


class PostSerializer(serializers.ModelSerializer):
    '''
    Serializer for converting Post instances into JSON data and vice-versa.
    owner - read-only field to display the username of the post's owner.
    '''
    owner = serializers.ReadOnlyField(
        source='owner.username')  #

    class Meta:
        '''
        Additional settings for the PostSerializer.
        model - specifies the model to serialize.
        fields - specifies the fields to include in the serialized representation.
        '''
        model = Post
        fields = ['id', 'title', 'body', 'owner', 'comments']


class UserSerializer(serializers.ModelSerializer):
    '''
    Serializer for converting User instances into JSON data and vice-versa.
    posts - read-only field to display all posts related to the user.
    '''
    posts = serializers.PrimaryKeyRelatedField(many=True,
                                               read_only=True)

    class Meta:
        '''
        Additional settings for the UserSerializer.
        model - specifies the model to serialize.
        '''
        model = User
        fields = ['id', 'username', 'posts', 'comments',
                  'categories']


class CommentSerializer(serializers.ModelSerializer):
    '''
    Serializer for converting Comment instances into JSON data and vice-versa.
    '''
    owner = serializers.ReadOnlyField(
        source='owner.username')

    class Meta:
        '''
        Additional settings for the CommentSerializer.
        model - specifies the model to serialize.
        '''
        model = Comment
        fields = ['id', 'body', 'owner', 'post']


class CategorySerializer(serializers.ModelSerializer):
    '''
    Serializer for converting Category instances into JSON data and vice-versa.
    '''
    owner = serializers.ReadOnlyField(
        source='owner.username')
    posts = serializers.PrimaryKeyRelatedField(many=True,
                                               read_only=True)

    class Meta:
        '''
        Additional settings for the CategorySerializer.
        '''
        model = Category
        fields = ['id', 'name', 'owner', 'posts']


