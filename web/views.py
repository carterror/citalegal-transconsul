from django.shortcuts import render
from .models import Testimonio, Trabajador
from usuarios.models import Usuario
from citas.models import Tramite, Cita, Disponible
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from configs.middleware import login_required, staff_member_required
from django.urls import reverse_lazy
from blog.models import Post
from django.http import JsonResponse
from django.db.models import Sum
from django.db.models import Q
from datetime import datetime
import json
from datetime import date
today = date.today()

def home(request):
    context = {
        "testimonios" : Testimonio.objects.all(),
        "trabajadores" : Trabajador.objects.all(),
        "tramites": Tramite.objects.all(),
        "posts": Post.objects.all(),
    }
    return render(request, 'web/pages/home.html', context)
 
def service(request):
    context = {
        "tramites": Tramite.objects.all(),
    }
    return render(request, 'web/pages/service.html', context)

def about(request):
    context = {
        "testimonios" : Testimonio.objects.all(),
    }
    return render(request, 'web/pages/about.html', context)

def testimoniof(request):
    context = {
        "testimonios" : Testimonio.objects.all(),
    }
    return render(request, 'web/pages/testimonio.html', context)

def blog(request):
    context = {
        "posts": Post.objects.all(),
    }
    return render(request, 'web/pages/blog.html', context)

@login_required
def profile(request):
    return render(request, 'web/profile.html')

@login_required
def reservar(request):
    context = {
        "tramites": Tramite.objects.all()
    }
    return render(request, 'web/cita.html', context)

@login_required
@staff_member_required
def dashboard(request):

    # Consulta y mapeo de campos
    citas_dict = Cita.objects.all()
    
    # Cambiar la clave 'descripcion' a 'title'
    citas_actualizadas = [
        {"title": cita.get_client[0], "client": cita.get_client[1], "status": cita.estado, "start":  cita.get_date.strftime("%Y-%m-%d"), "backgroundColor": "green" if cita.estado == "success" else ("orange" if cita.estado == "accept" else "red"), "borderColor": "green" if cita.estado == "success" else ("orange" if cita.estado == "accept" else "red") } for cita in citas_dict
    ]

    print(citas_actualizadas)
    context = {
        "count_user" : Usuario.objects.count(),
        "count_citas_c" : Cita.objects.filter(estado='success').count(),
        "count_citas_p" : Cita.objects.filter(Q(estado='accept') | Q(estado='pending')).count(),
        "disponi": Disponible.objects.filter(fecha__contains=today).aggregate(disponi=Sum('disponible')-Sum('reservas')),
        "calendar": json.dumps(citas_actualizadas),
        "citas_estados": [
            Cita.objects.filter(estado='success').count(),
            Cita.objects.filter(estado='pending').count(),
            Cita.objects.filter(estado='cancel').count(),
            Cita.objects.filter(estado='accept').count()
        ]
    }
    return render(request, 'madmin/dash.html', context)

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
    

@login_required
@staff_member_required
def usuario(request):
    context = {
        'usuarios': Usuario.objects.all()
    }

    return render(request, 'madmin/usuario/index.html', context)

@login_required
@staff_member_required
def updateUsuario(request, pk, type):
    usuario = get_object_or_404(Usuario, pk=pk)  

    if type == 'deactive':
        usuario.is_active = not usuario.is_active
    if type == 'staff':
        usuario.is_staff = not usuario.is_staff
    
    usuario.save()

    messages.success(request, 'Guardado con éxito')
    return redirect(reverse_lazy('usuario'))

def showArt(request, slug):
    post = get_object_or_404(Post, slug=slug)  
    posts = Post.objects.exclude(id=post.id).all().order_by('-id')[:5]
    context = {
        "post" : post,
        "posts" : posts
    }
    return render(request, 'web/pages/article.html', context)