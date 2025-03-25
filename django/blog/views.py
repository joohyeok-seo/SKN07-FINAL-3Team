from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404


from .models import Post, Comment
from .form import CommentForm



# Create your views here.
class PostList(ListView):
    model = Post
    template_name = 'blog/post_list.html'

    ordering = '-pk'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        # context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter().count()
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        # context['categories'] = Category.objects.all()
        # category 에러 발생함.
        # context['no_category_post_count'] = Post.objects.filter(category=None).count()
        context['no_category_post_count'] = Post.objects.filter().count()
        context['comment_form'] = CommentForm
        return context

class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/create_new_post.html'
    fields = [
        'title', 'content', 'head_image', 'file_upload'
    ]

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            response = super(CreatePost, self).form_valid(form)

            return response
        else:
            return redirect('/blog/')

class CommentUpdate(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(CommentUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

def new_comment(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk)

        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                return redirect(comment.get_absolute_url())
        else:
            return redirect(post.get_absolute_url())
    else:
        raise PermissionDenied
    
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post = comment.post
    if request.user.is_authenticated and request.user == comment.author:
        comment.delete()
        return redirect(post.get_absolute_url())
    else:
        raise PermissionDenied