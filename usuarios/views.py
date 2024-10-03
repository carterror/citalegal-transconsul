from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from .models import Usuario
from django.contrib import messages
from django.core.mail import send_mail
from allauth.account.models import EmailAddress

from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_user_mail(request):
    subject = 'Cita Legal' 
    html_message = render_to_string('emails/mail_template.html', {'message': 'Hello!'})
    plain_message = strip_tags(html_message)
    # Note that above we are reading content from an HTML file 
    from_email = 'no.responder.correo.98@gmail.com'

    to = 'carlos.bramila98@gmail.com' 

    response = send_mail(subject, plain_message, from_email, [to], html_message=html_message)
    
    return HttpResponse(response)

def signin(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse_lazy('home'))
        else:
            return redirect(reverse_lazy('login'))
    
    return render(request, 'web/login.html')

def changePassword(request):
    user = authenticate(request, username=request.user.username, password=request.POST['password'])
    if user is None:
        messages.error(request, 'Contraseña actual incorrecta')
    elif request.POST['password1'] != request.POST['password2'] or not (request.POST['password1'] or request.POST['password2']):
        messages.error(request, 'Las contraseñas no coinciden')
    else:
        user = Usuario.objects.get(pk=request.user.id)
        user.set_password(request.POST['password1'])
        user.save()
        login(request, user)
        messages.success(request, 'Contraseña actualizada')

    return redirect(reverse_lazy('profile'))

def updatePerfil(request):
    user = Usuario.objects.get(pk=request.user.id)
    
    user.first_name = request.POST['nombre']
    user.last_name = request.POST['apellido']
    user.ci = request.POST['ci']
    user.telefono = request.POST['telefono']
    user.direccion = request.POST['direccion']

    user.save()

    messages.success(request, 'Información actualizada')

    return redirect(reverse_lazy('profile'))

def updatePhotoPerfil(request):
    images = request.FILES.getlist('foto')

    if images:
        user = Usuario.objects.get(pk=request.user.id)
        user.avatar = images[0]
        user.save()

    messages.success(request, 'Foto actualizada')

    return redirect(reverse_lazy('profile'))

def confirmEmail(request):
    email = EmailAddress.objects.filter(user=1).first()
    email.set_as_primary()
    email.set_verified()
    email.save()
    return HttpResponse(1)