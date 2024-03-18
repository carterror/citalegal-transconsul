from django.shortcuts import render
from django.views.generic import ListView, DeleteView, DetailView, CreateView
from blog.models import Post
from blog.forms import PostForm

# Create your views here.
class PostList(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    paginate_by = 6
    context_object_name = "post_list"

    def get_queryset(self, **kwargs):
        return Post.objects.filter(presentar=True).order_by("-publicado")


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        return context

class PostCreate(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_create.html'
    
class PostDelete(DeleteView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_create.html'