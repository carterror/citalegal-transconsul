from django.urls import path
from citas import views as viewCita

urlpatterns = [
    path('disponible/', viewCita.disponible, name='disponible'),
    path('disponible/store/', viewCita.storeDisponible, name='storeDisponible'),
    path('disponible/<int:pk>/update/', viewCita.updateDisponible, name='updateDisponible'),
    path('disponible/<int:pk>/delete/', viewCita.deleteDisponible, name='deleteDisponible'),

    path('tramite/', viewCita.tramite, name='tramite'),
    path('tramite/store/', viewCita.storeTramite, name='storeTramite'),
    path('tramite/<int:pk>/update/', viewCita.updateTramite, name='updateTramite'),
    path('tramite/<int:pk>/delete/', viewCita.deleteTramite, name='deleteTramite'),

    path('reserva/', viewCita.cita, name='citas'),

    path('reserva/store/', viewCita.storeCita, name='storeCita'),
    path('reserva/<int:pk>/aceptar/', viewCita.aceptarCita, name='aceptarCita'),
    path('reserva/<int:pk>/cancelar/', viewCita.cancelarCita, name='cancelarCita'),

]
