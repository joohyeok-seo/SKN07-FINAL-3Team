from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from markdownx.utils import markdown



# Create your models here.
class Foods(models.Model):
    title = models.CharField(max_length=50)
    hook_text = models.CharField(max_length=100, blank=True)
    content = MarkdownxField()
    summarize_content = models.CharField(max_length=1000, blank=True)

    head_image = models.ImageField(
        upload_to='foods/images/%Y/%m/%d/', blank=True
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    
    # category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    # tags = models.ManyToManyField(Tag, blank=True)
    
    def get_absolute_url(self):
        return f'/foods/{self.pk}/'
    
    def get_content_markdown(self):
        return markdown(self.content)

    def __str__(self):
        return f'[{self.pk}] {self.title} :: {self.author}'