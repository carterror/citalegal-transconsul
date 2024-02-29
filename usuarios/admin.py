from django.contrib import admin
from usuarios.models import Usuario

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'last_name',
        'is_superuser'
    )
    
    # campos que se pueden editar
    fieldsets = (
        (None, {
            'fields': ('username', 'email',)
        }),
        ('Informacion Personal', {
            'fields': ('first_name', 'last_name',)
        }),
        ('Permisos', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups')
        }),
        ('Fechas', {
            'fields': ('last_login', 'date_joined')
        }),
    )
    

admin.site.register(Usuario,UserAdmin)
