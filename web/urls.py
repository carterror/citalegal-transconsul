"""
URL configuration for citalegal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from citas import views
from .views import home, service, about, testimonio, blog, dashboard, trabajador, cita, storeTrabajador, updateTrabajador, deleteTrabajador, profile
from usuarios.views import changePassword, updatePerfil, updatePhotoPerfil

urlpatterns = [
    path('aceptar/<int:pk>', views.CustomView.as_view(), name='aceptar_cita'),
    path('', home, name='home'),
    path('admin', dashboard, name='home'),
    path('service', service, name='service'),
    path('about', about, name='about'),
    path('testimonio', testimonio, name='testimonio'),
    path('blog', blog, name='blog'),

    path('profile/', profile, name='profile'),
    path('profile/change-password/', changePassword, name='changePassword'),
    path('profile/update/', updatePerfil, name='updatePerfil'),
    path('profile/update-photo/', updatePhotoPerfil, name='updatePhotoPerfil'),

    path('citas/', cita, name='citas'),


    
    path('admin/trabajadores/', trabajador, name='trabajador'),
    path('admin/trabajadores/store/', storeTrabajador, name='storeTrabajador'),
    path('admin/trabajadores/<int:pk>/update/', updateTrabajador, name='updateTrabajador'),
    path('admin/trabajadores/<int:pk>/delete/', deleteTrabajador, name='deleteTrabajador'),


]
