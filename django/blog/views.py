from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post
from .form import CommentForm



# Create your views here.
class PostList(ListView):
    model = Post
    template_name = 'blog/index.html'

class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post.html'
    
    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        # context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        context['comment_form'] = CommentForm
        return context