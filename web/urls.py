from django.urls import path
from citas import views as viewCitas
from .views import (home, service, about, testimoniof, blog, dashboard, trabajador, 
                    reservar, storeTrabajador, updateTrabajador, deleteTrabajador, profile,
                    storeTestimonio, deleteTestimonio, testimonio, deleteAllTrabajador, 
                    deleteAllTestimonios, usuario, updateUsuario, showArt)
from usuarios.views import changePassword, updatePerfil, updatePhotoPerfil

urlpatterns = [

    path('', home, name='home'),
    path('admin/', dashboard, name='admin'),

    path('service', service, name='showService'),
    path('about', about, name='showAbout'),
    path('testimonio', testimoniof, name='showtestimonio'),
    path('blog', blog, name='showBlog'),
    path('blog/<slug:slug>', showArt, name='showArt'),


    path('profile/', profile, name='profile'),
    path('profile/change-password/', changePassword, name='changePassword'),
    path('profile/update/', updatePerfil, name='updatePerfil'),
    path('profile/update-photo/', updatePhotoPerfil, name='updatePhotoPerfil'),

    path('reservar/', reservar, name='reservar'),
    path('citas/show', viewCitas.showCita, name='showCita'),

    path('admin/trabajadores/', trabajador, name='trabajador'),
    path('admin/trabajadores/store/', storeTrabajador, name='storeTrabajador'),
    path('admin/trabajadores/<int:pk>/update/', updateTrabajador, name='updateTrabajador'),
    path('admin/trabajadores/<int:pk>/delete/', deleteTrabajador, name='deleteTrabajador'),
    path('admin/trabajadores/delete-all/', deleteAllTrabajador, name='deleteAllTrabajador'),

    path('admin/usuarios/', usuario, name='usuario'),
    path('admin/usuarios/<int:pk>/<str:type>/', updateUsuario, name='updateUsuario'),

    path('admin/testimonios/', testimonio, name='testimonio'),
    path('admin/testimonios/store/', storeTestimonio, name='storeTestimonio'),
    path('admin/testimonios/<int:pk>/delete/', deleteTestimonio, name='deleteTestimonio'),
    path('admin/testimonios/delete-all/', deleteAllTestimonios, name='deleteAllTestimonios'),

]
