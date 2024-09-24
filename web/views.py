from django.shortcuts import render
from .models import Testimonio, Trabajador
from usuarios.models import Usuario
from citas.models import Tramite
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from configs.middleware import login_required, staff_member_required
from django.urls import reverse_lazy
from blog.models import Post
from django.http import JsonResponse
import json

def home(request):
    context = {
        "testimonios" : Testimonio.objects.all(),
        "trabajadores" : Trabajador.objects.all(),
        "tramites": Tramite.objects.all(),
        "posts": Post.objects.all(),
    }
    return render(request, 'web/pages/home.html', context)
 
def service(request):
    return render(request, 'web/pages/service.html')

def about(request):
    return render(request, 'web/pages/about.html')

def testimoniof(request):
    return render(request, 'web/pages/testimonio.html')

def blog(request):
    return render(request, 'web/pages/blog.html')

@login_required
def profile(request):
    return render(request, 'web/profile.html')

@login_required
def reservar(request):
    context = {
        "tramites": Tramite.objects.all()
    }
    return render(request, 'web/cita.html', context)

@staff_member_required
def dashboard(request):

    context = {
        "trabajadores" : Trabajador.objects.all(),
    }
    return render(request, 'madmin/blank.html', context)

@login_required
@staff_member_required
def dashboard(request):
    context = {
        "trabajadores" : Trabajador.objects.all(),
    }
    return render(request, 'madmin/blank.html', context)

@login_required
@staff_member_required
def trabajador(request):
    context = {
        'trabajadores': Trabajador.objects.all()
    }

    return render(request, 'madmin/trabajador/index.html', context)

@login_required
@staff_member_required
def storeTrabajador(request):
    images = request.FILES.getlist('foto')
    
    trabajador = Trabajador.objects.create(
        descripcion = request.POST['descripcion'],
        nombre = request.POST['nombre'],
        nivel = request.POST['nivel'],
        foto = images[0] if images else None
    )

    messages.success(request, 'Guardado con éxito')
    return redirect(reverse_lazy('trabajador'))

@login_required
@staff_member_required
def updateTrabajador(request, pk):
    trabajador = get_object_or_404(Trabajador, pk=pk)
    images = request.FILES.getlist('foto')
    
    trabajador.descripcion = request.POST['descripcion']
    trabajador.nombre = request.POST['nombre']
    trabajador.nivel = request.POST['nivel']

    if images:
        trabajador.foto = images[0]

    trabajador.save()

    messages.success(request, 'Guardado con éxito')
    return redirect(reverse_lazy('trabajador'))


@login_required
@staff_member_required
def deleteTrabajador(request, pk):
    trabajador = get_object_or_404(Trabajador, pk=pk)

    trabajador.delete()
    
    messages.success(request, 'Eliminado con éxito.')
    
    return redirect('trabajador')

@login_required
@staff_member_required
def deleteAllTrabajador(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print(data)
            # Procesa los datos aquí
            for id in list(data):
                trabajador = get_object_or_404(Trabajador, pk=id)
                trabajador.delete()

            response_data = {'message': 'Datos eliminados correctamente'}

            return JsonResponse(response_data, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Datos JSON inválidos'}, status=400)

    else:

        messages.success(request, 'Eliminado con éxito.')
        
        return redirect(reverse_lazy('trabajador'))


@login_required
@staff_member_required
def testimonio(request):
    context = {
        'testimonios': Testimonio.objects.all(),
    }

    return render(request, 'madmin/testimonio/index.html', context)

@login_required
def storeTestimonio(request):
    count_testi = Testimonio.objects.filter(user=request.user).count()
    if count_testi > 0:
        messages.error(request, 'Ya usted dejó su testimonio.')
    else:
        testimonio = Testimonio.objects.create(
            user = request.user,
            comentario = request.POST['comentario'],
            servicio = request.POST['servicio'],
        )

        messages.success(request, 'Guardado con éxito')
    return redirect(reverse_lazy('home'))

@login_required
@staff_member_required
def deleteTestimonio(request, pk):
    testimonio = get_object_or_404(Testimonio, pk=pk)

    testimonio.delete()
    
    messages.success(request, 'Eliminado con éxito.')
    
    return redirect('testimonio')


@login_required
@staff_member_required
def deleteAllTestimonios(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print(data)
            # Procesa los datos aquí
            for id in list(data):
                testimonio = get_object_or_404(Testimonio, pk=id)
                testimonio.delete()

            response_data = {'message': 'Datos eliminados correctamente'}

            return JsonResponse(response_data, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Datos JSON inválidos'}, status=400)

    else:

        messages.success(request, 'Eliminado con éxito.')
        
        return redirect(reverse_lazy('testimonio'))
