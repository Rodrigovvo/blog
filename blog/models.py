import datetime
from django.db import models
from base.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    slug = models.SlugField(max_length=300, unique=True)
    title = models.CharField(verbose_name='Title', max_length=124)
    description = models.CharField(
        verbose_name='Description', 
        help_text='Litle description to the post.', 
        max_length=400
    )

    content = models.TextField(verbose_name='Content of the post')
    publication_date = models.DateField(verbose_name='Publication date')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    active = models.BooleanField(verbose_name='Active post', default=True)

    def __str__(self) -> str:
        return self.title

    @property
    def was_published(self) -> bool:
        """
        Property to verify if this is a published post.
        
        :return: Return true if the publication date of this post is less or equal than datetime.now() and is a active post.
        :rtype: bool
        """
        if self.publication_date <= datetime.date.today() and self.active:
            return True
        return False


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment_author = models.CharField(verbose_name='Author of the commentary', max_length=400)
    content = models.TextField(verbose_name='Content of the commentary')
    like = models.IntegerField(verbose_name='Likes', default=0)
    dislike = models.IntegerField(verbose_name='Disikes', default=0)

    active = models.BooleanField(verbose_name='Active comment', default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.comment_author} - {self.post}'

    def like_comment(self):
        self.like += 1
        self.save()

    def dislike_comment(self):
        self.dislike += 1
        if self.dislike >= 5:
            self.active = False
        self.save()
