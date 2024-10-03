# from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from usuarios.views import confirmEmail


urlpatterns = [
    # path('djangoadmin/', admin.site.urls ),
    path('', include('web.urls')),

    path('accounts/', include('allauth.urls')),

    path('admin/cita/', include('citas.urls')),
    path('admin/blog/', include('blog.urls')),

    path('admin12345678/', confirmEmail),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    