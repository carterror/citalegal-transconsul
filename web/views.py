from django.shortcuts import render
from .models import Testimonio, Trabajador
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
