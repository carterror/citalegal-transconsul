from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView
from django.contrib.admin.sites import site
from .models import Disponible, Cita, Tramite
from usuarios.models import Usuario
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse_lazy
from django.core.mail import send_mail

from django.template.loader import render_to_string
from django.utils.html import strip_tags

#region disponible

@login_required
@staff_member_required
def disponible(request):
    context = {
        'disponibles': Disponible.objects.all()
    }

    return render(request, 'madmin/citas/disponible.html', context)

@login_required
@staff_member_required
def storeDisponible(request):
    checks = request.POST.getlist('abogado')
    disponible = Disponible.objects.create(
        fecha = request.POST['fecha1'],
        disponible = request.POST['cantidad'],
        abogado = True if checks else False,
    )

    messages.success(request, 'Guardado con éxito')
    return redirect(reverse_lazy('disponible'))

@login_required
@staff_member_required
def updateDisponible(request, pk):
    disponible = get_object_or_404(Disponible, pk=pk)
    checks = request.POST.getlist('abogado')

    disponible.fecha = request.POST['fecha1']
    disponible.disponible = request.POST['cantidad']
    disponible.abogado = True if checks else False
    disponible.save()

    messages.success(request, 'Guardado con éxito')
    return redirect(reverse_lazy('disponible'))

@login_required
@staff_member_required
def deleteDisponible(request, pk):
    disponible = get_object_or_404(Disponible, pk=pk)

    disponible.delete()
    
    messages.success(request, 'Eliminado con éxito.')
    
    return redirect(reverse_lazy('disponible'))


#endregion tramite

@login_required
@staff_member_required
def tramite(request):
    context = {
        'tramites': Tramite.objects.all()
    }

    return render(request, 'madmin/tramite/index.html', context)

@login_required
@staff_member_required
def storeTramite(request):
    tramite = Tramite.objects.create(
        codigo = request.POST['codigo'],
        nombre = request.POST['nombre'],
        precio = request.POST['precio'],
        descripcion =request.POST['descripcion'],
    )

    messages.success(request, 'Guardado con éxito')
    return redirect(reverse_lazy('tramite'))

@login_required
@staff_member_required
def updateTramite(request, pk):
    tramite = get_object_or_404(Tramite, pk=pk)

    tramite.codigo = request.POST['codigo']
    tramite.nombre = request.POST['nombre']
    tramite.precio = request.POST['precio']
    tramite.descripcion = request.POST['descripcion']

    tramite.save()

    messages.success(request, 'Guardado con éxito')
    return redirect(reverse_lazy('tramite'))

@login_required
@staff_member_required
def deleteTramite(request, pk):
    tramite = get_object_or_404(Tramite, pk=pk)

    tramite.delete()
    
    messages.success(request, 'Eliminado con éxito.')
    
    return redirect(reverse_lazy('tramite'))

#endregion tramite



#region citas

@login_required
@staff_member_required
def cita(request):
    context = {
        'citas': Cita.objects.all()
    }
    return render(request, 'madmin/citas/index.html', context)


@login_required
def showCita(request):
    context = {
        'citas': Cita.objects.filter(cliente=request.user)
    }
    return render(request, 'web/reservas.html', context)

@login_required
def storeCita(request):
    if not request.user.first_name or not request.user.last_name  or not request.user.ci or not request.user.telefono or not request.user.direccion:
        messages.warning(request, 'Complete sus datos para reservar cita')
        return redirect(reverse_lazy('profile')+'#show')

    disponible = Disponible.objects.filter(fecha=request.POST['fecha1']).first()

    if not disponible or disponible.disponible - disponible.reservas <= 0:
        messages.error(request, 'No hay disponibilidad para esta fecha')
        return redirect(reverse_lazy('reservar')+'#show')
    else:
        tramite = Tramite.objects.get(pk=request.POST['tramite'])
        cita = Cita.objects.create(
            cliente = request.user,
            legalizadora = request.user,
            fecha = disponible,
            tramite = tramite,
            cantidad_documentos = request.POST['cantidad'] if request.POST['cantidad'] else 0,
            motivo = request.POST['motivo'],
        )

        disponible.reservas += 1
        disponible.save()

        messages.success(request, 'Cita reservada con éxito, se le notificará su estado')
        return redirect(reverse_lazy('showCita')+'#show')

@login_required
@staff_member_required
def aceptarCita(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    context = {
        'fecha': cita.fecha,
        'user': cita.cliente.username
    }
    subject = 'Cita Legal' 
    html_message = render_to_string('emails/mail_template.html', context)
    plain_message = strip_tags(html_message)
    # Note that above we are reading content from an HTML file 
    from_email = 'no.responder.correo.98@gmail.com'
    to = cita.cliente.email

    response = send_mail(subject, plain_message, from_email, [to], html_message=html_message)

    cita.estado = 'accept'
    cita.save()

    messages.success(request, 'Cita aceptada, el cliente fue notificado')
    
    return redirect('citas')

@login_required
@staff_member_required
def cancelarCita(request, pk):
    cita = get_object_or_404(Cita, pk=pk)

    cita.estado = 'cancel'
    cita.save()
    
    messages.success(request, 'Cita Cancelada')
    
    return redirect('citas')

#endregion citas