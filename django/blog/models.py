from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    hook_text = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    summarize_content = models.CharField(max_length=1000, blank=True)

    head_image = models.ImageField(
        upload_to='blog/images/%Y/%m/%d/', blank=True
    )
    file_upload = models.FileField(
        upload_to='blog/files/%Y/%m/%d', blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    
    # category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    # tags = models.ManyToManyField(Tag, blank=True)
    
    def go2page(self):
        return f'/blog/{self.pk}/'

    def __str__(self):
        return f'[{self.pk}] {self.title} :: {self.author}'
    
class Comment(models.Model):
    post = models.ForeignKey(Post, null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(null=True, blank=True, default=None)

    def __str__(self):
        return f'{self.author}::{self.content}'
    
    def get_absolute_url(self):
        return f'{self.post.get_absolute_url()}#comment-{self.pk}'

    def get_avatar_url(self):
        if self.author.socialaccount_set.exists():
            return self.author.socialaccount_set.first().get_avatar_url()
        else:
            return f'https://api.adorable.io/avatars/60/{ f"{self.author.username[:2].upper()}" }.png'