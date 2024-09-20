from django.shortcuts import render
from django.views.generic import ListView, DeleteView, DetailView, CreateView
from blog.models import Post
from blog.forms import PostForm
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView
from django.contrib.admin.sites import site
from usuarios.models import Usuario
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse_lazy

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




@login_required
@staff_member_required
def blog(request):
    context = {
        'blogs': Post.objects.all()
    }

    return render(request, 'madmin/blog/index.html', context)

@login_required
@staff_member_required
def storeBlog(request):
    blog = Post.objects.create(
        titulo = request.POST['titulo'],
        cuerpo = request.POST['descri'],
        autor = request.user
    )

    messages.success(request, 'Guardado con éxito')
    return redirect('blog')

@login_required
@staff_member_required
def updateBlog(request, pk):
    blog = get_object_or_404(Post, pk=pk)

    blog.codigo = request.POST['codigo']
    blog.nombre = request.POST['nombre']
    blog.precio = request.POST['precio']
    blog.descripcion = request.POST['descripcion']

    blog.save()

    messages.success(request, 'Guardado con éxito')
    return redirect('blog')

@login_required
@staff_member_required
def deleteBlog(request, pk):
    blog = get_object_or_404(Post, pk=pk)

    blog.delete()
    
    messages.success(request, 'Eliminado con éxito.')
    
    return redirect('blog')