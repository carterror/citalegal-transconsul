# from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from usuarios.views import onrender, send_user_mail, home, service, about, testimonio, blog

urlpatterns = [
    # path('djangoadmin/', admin.site.urls ),
    path('', include('web.urls')),

    path('accounts/', include('allauth.urls')),

    path('admin/cita/', include('citas.urls')),
    path('admin/blog/', include('blog.urls')),

    path('test/', send_user_mail),
    # path("login/", signin, name='login'),
    path('', home, name='home'),
    path('service', service, name='service'),
    path('about', about, name='about'),
    path('testimonio', testimonio, name='testimonio'),
    path('blog', blog, name='blog'),
    path('render', onrender)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    