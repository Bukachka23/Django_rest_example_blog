
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    # URL pattern for listing all users or creating a new user
    path('users/', views.UserList.as_view()),

    # URL pattern for retrieving, updating, or deleting a single user based on their primary key (pk)
    path('users/<int:pk>', views.UserList.as_view()),

    # URL pattern for listing all posts or creating a new post
    path('posts/', views.PostList.as_view()),

    # URL pattern for retrieving, updating, or deleting a single post based on its primary key (pk)
    path('posts/<int:pk>', views.PostDetail.as_view()),

    # URL pattern for listing all comments or creating a new comment
    path('comments/', views.CommentList.as_view()),

    # URL pattern for retrieving, updating, or deleting a single comment based on its primary key (pk)
    path('comments/<int:pk>', views.CommentDetail.as_view()),

    # URL pattern for listing all categories or creating a new category
    path('category/', views.CategoriesList.as_view()),

    # URL pattern for retrieving, updating, or deleting a single category based on its primary key (pk)
    path('category/<int:pk>', views.CategoriesDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
