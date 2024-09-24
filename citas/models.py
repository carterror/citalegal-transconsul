from django.db import models

from usuarios.models import Usuario
from django.contrib.auth.models import User
# Create your models here.

# TODO
# replanificacion de citas, con secretaria, ausente(no presentado) 
ESTADOS = [
        ('pending', 'Pendiente'),
        ('cancel', 'Cancelada'),
        ('accept', 'Aceptada'),
        ('success', 'Completada'),
]

class Disponible(models.Model):
    disponible = models.IntegerField(default=10, null=False)
    reservas = models.IntegerField(default=0)
    abogado = models.BooleanField(default=False)
    fecha = models.DateTimeField('Fecha', null=True)
    created_at = models.DateTimeField('Creado', auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return str(self.created_at)
    
    
class Tramite(models.Model):
    nombre = models.CharField(max_length=250)
    precio = models.DecimalField(decimal_places=2, max_digits=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
      
    def __str__(self) -> str:
        return self.nombre  
