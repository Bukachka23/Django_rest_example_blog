from django.db import models


class Post(models.Model):
    '''
    Defines the Post model that represents a blog post.
    created - automatically set when a Post instance is created.
    title - title of the post, can be blank.
    body - main content of the post, can be blank.
    owner - user who owns the post.
    '''
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    categories = models.ManyToManyField('Category', related_name='posts')

    class Meta:
        '''
        Additional settings for the Post model.
        ordering -  used to order the comments by the 'created' field when queried.
        '''
        ordering = ('created',)


class Comment(models.Model):
    '''
    Defines the Comment model that represents a comment on a blog post.
    '''
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    owner = models.ForeignKey('auth.User', related_name='comments',
                              on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments',
                             on_delete=models.CASCADE)

    class Meta:
        '''
        Additional settings for the Comment model.

        '''
        ordering = ('created',)


class Category(models.Model):
    '''
    Defines the Category model that represents a category for organizing blog posts.
    name - name of the category.
    '''
    name = models.CharField(max_length=100)
    owner = models.ForeignKey('auth.User', related_name='categories',
                              on_delete=models.CASCADE)

    def __str__(self):
        '''
        String representation of the Category model.
        '''
        return self.name
