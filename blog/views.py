from django.shortcuts import render
from blog.models import Post

from django.shortcuts import render, redirect

from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse_lazy
from django.http import JsonResponse
import json

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
    images = request.FILES.getlist('foto')

    blog = Post.objects.create(
        titulo = request.POST['titulo'],
        cuerpo = request.POST['descri'],
        autor = request.user,
        foto = images[0] if images else None
    )

    messages.success(request, 'Guardado con éxito')
    return redirect('blog')

@login_required
@staff_member_required
def updateBlog(request, pk):
    blog = get_object_or_404(Post, pk=pk)
    images = request.FILES.getlist('foto')

    blog.titulo = request.POST['titulo']
    blog.cuerpo = request.POST['descri']
    if images:
        blog.foto = images[0]
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

@login_required
@staff_member_required
def deleteAllBlog(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            for id in list(data):
                blog = get_object_or_404(Post, pk=id)
                blog.delete()

            response_data = {'message': 'Datos eliminados correctamente'}

            return JsonResponse(response_data, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Datos JSON inválidos'}, status=400)

    else:

        messages.success(request, 'Eliminado con éxito.')
        return redirect('blog')