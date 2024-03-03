from django.contrib import admin
from citas.models import Cita, Tramite
from django.contrib import messages

# Register your models here.

admin.site.register(Tramite)

@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    
    list_display = (
        'created_at',
        'cliente',
        'legalizadora',
        'catidad_documentos',
        'lugar',
        'fecha',
    )
    
    date_hierarchy = 'created_at'
    list_filter = ('cliente', 'legalizadora')

    search_fields = ('cliente__first_name','cliente__last_name')
    # campos que se pueden editar
    # fieldsets = (
    #     (None, {
    #         'fields': ('cliente', 'legalizadora',)
    #     }),
    # )
    @admin.display(ordering='last_name', description='Clienterrrrrrrr')
    def cliente(self, obj):
        return obj.cliente.name
    
    def aceptarCita(modeladmin, request, queryset):
        if queryset.get().fecha != None:
            messages.error(request, "Solo se puede aceptar una cita a la vez")
            return
        
        queryset.update(fecha='2028-10-22')
        messages.success(request, "Se aceptó la cita")
        
    admin.site.add_action(aceptarCita, "Aceptar Cita")