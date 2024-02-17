from django.db import models

from usuarios.models import Usuario

# Create your models here.

class Cita(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='clientes')
    legalizadora = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='legalizadoras')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)