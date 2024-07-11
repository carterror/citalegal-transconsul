from django.contrib import admin
from .models import Trabajador, Testimonio
# Register your models here.
admin.site.register(Testimonio)
@admin.register(Trabajador)
class CitaAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'nivel',
        'descripcion',
        'created_at'
    )
    
