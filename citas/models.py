from django.db import models

from usuarios.models import Usuario

# Create your models here.

class Cita(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='clientes')
    legalizadora = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='legalizadoras')
    catidad_documentos = models.IntegerField(null=True)
    obtencion = models.BooleanField(default=False)
    lugar = models.CharField(max_length=250, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
class Tramite(models.Model):
    nombre = models.CharField(max_length=250)
    precio = models.DecimalField(decimal_places=2, max_digits=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
