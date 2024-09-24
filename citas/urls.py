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

urlpatterns = [
    path('aceptar/<int:pk>', views.CustomView.as_view(), name='aceptar_cita'),

    path('disponible/', views.disponible, name='disponible'),
    path('disponible/store/', views.storeDisponible, name='storeDisponible'),
    path('disponible/<int:pk>/update/', views.updateDisponible, name='updateDisponible'),
    path('disponible/<int:pk>/delete/', views.deleteDisponible, name='deleteDisponible'),

    path('tramite/', views.tramite, name='tramite'),
    path('tramite/store/', views.storeTramite, name='storeTramite'),
    path('tramite/<int:pk>/update/', views.updateTramite, name='updateTramite'),
    path('tramite/<int:pk>/delete/', views.deleteTramite, name='deleteTramite'),

    path('citas/', views.cita, name='citas'),

    path('cita/store/', views.storeCita, name='storeCita'),
    path('cita/<int:pk>/aceptar/', views.aceptarCita, name='aceptarCita'),
    path('cita/<int:pk>/cancelar/', views.cancelarCita, name='cancelarCita'),

]
