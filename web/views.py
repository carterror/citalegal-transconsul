from django.shortcuts import render
from .models import Testimonio, Trabajador
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.

def home(request):
    context = {
        "testimonios" : Testimonio.objects.all(),
        "trabajadores" : Trabajador.objects.all(),
    }
    return render(request, 'web/pages/home.html', context)
 
def service(request):
    return render(request, 'web/pages/service.html')

def about(request):
    return render(request, 'web/pages/about.html')

def testimonio(request):
    return render(request, 'web/pages/testimonio.html')

def blog(request):
    return render(request, 'web/pages/blog.html')

def profile(request):
    return render(request, 'web/profile.html')

def cita(request):
    return render(request, 'web/cita.html')

@login_required
@staff_member_required
def dashboard(request):
    messages.warning(request, 'asfqwiufbqwiufbwqoiu fbwqouibiou isbduiqwbdi')
    context = {
        "trabajadores" : Trabajador.objects.all(),
    }
    return render(request, 'madmin/blank.html', context)

@login_required
@staff_member_required
def dashboard(request):
    messages.success(request, 'asfqwiufbqwiufbwqoiu fbwqouibiou isbduiqwbdi')
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
    if images:
        trabajador = Trabajador.objects.create(
        descripcion = request.POST['descripcion'],
        nombre = request.POST['nombre'],
        nivel = request.POST['nivel'],
        foto = images[0]
    )
    else:
        trabajador = Trabajador.objects.create(
        descripcion = request.POST['descripcion'],
        nombre = request.POST['nombre'],
        nivel = request.POST['nivel'],
    )

    messages.success(request, request.POST)
    return redirect('trabajador')

@login_required
@staff_member_required
def updateTrabajador(request, pk):
    trabajador = get_object_or_404(Trabajador, pk=pk)
    trabajador.descripcion = request.POST['descripcion']
    trabajador.nombre = request.POST['nombre']
    trabajador.nivel = request.POST['nivel']
    trabajador.save()
    messages.success(request, trabajador)
    return redirect('trabajador')

@login_required
@staff_member_required
def deleteTrabajador(request, pk):
    trabajador = get_object_or_404(Trabajador, pk=pk)

    trabajador.delete()
    
    messages.success(request, 'Eliminado con éxito.')
    
    return redirect('trabajador')