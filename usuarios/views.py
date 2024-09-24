from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from .models import Usuario
from django.contrib import messages



def send_user_mail(request):
    subject, from_email, to = "Cita Legal", settings.EMAIL_HOST_USER, "carlos.bramila98@gmail.com"
    text_content = "This is an important message."
    html_content = '''
    <img src="file:///D:/Proyects/citalegal-transconsul/legalcare-master/index.html" alt="Cita Legal" style="width: 100px; height: 100px;">
    <h1>¡Hola!</h1>
    <p>Este es un mensaje de prueba.</p>
    <p>Gracias por tu atención.</p>
    <p>Saludos.</p>
    '''
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    
    
    return HttpResponse(msg.send())

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