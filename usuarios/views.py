from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login


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

def home(request):
    return render(request, 'web/pages/home.html')
 
def service(request):
    return render(request, 'web/pages/service.html')

def about(request):
    return render(request, 'web/pages/about.html')

def testimonio(request):
    return render(request, 'web/pages/testimonio.html')

def blog(request):
    return render(request, 'web/pages/blog.html')

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

