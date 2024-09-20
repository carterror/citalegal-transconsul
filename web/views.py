from django.shortcuts import render
from .models import Testimonio, Trabajador
from usuarios.models import Usuario
from citas.models import Tramite
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse_lazy

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

def testimoniof(request):
    return render(request, 'web/pages/testimonio.html')

def blog(request):
    return render(request, 'web/pages/blog.html')

def profile(request):
    return render(request, 'web/profile.html')

def reservar(request):
    context = {
        "tramites": Tramite.objects.all()
    }
    return render(request, 'web/cita.html', context)

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

    messages.success(request, 'Guardado con éxito')
    return redirect('trabajador')

@login_required
@staff_member_required
def updateTrabajador(request, pk):
    trabajador = get_object_or_404(Trabajador, pk=pk)
    
    trabajador.descripcion = request.POST['descripcion']
    trabajador.nombre = request.POST['nombre']
    trabajador.nivel = request.POST['nivel']
    trabajador.save()

    messages.success(request, 'Guardado con éxito')
    return redirect('trabajador')

@login_required
@staff_member_required
def deleteTrabajador(request, pk):
    trabajador = get_object_or_404(Trabajador, pk=pk)

    trabajador.delete()
    
    messages.success(request, 'Eliminado con éxito.')
    
    return redirect('trabajador')


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