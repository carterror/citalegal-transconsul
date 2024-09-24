from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from .models import Usuario
from django.contrib import messages
from django.core.mail import send_mail

from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_user_mail(request):
    subject = 'Cita Legal' 
    html_message = render_to_string('emails/mail_template.html', {'message': 'Hello!'})
    plain_message = strip_tags(html_message)
    # Note that above we are reading content from an HTML file 
    from_email = 'no-responder@transconsul.sa' 
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

