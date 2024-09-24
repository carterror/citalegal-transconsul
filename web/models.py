from django.db import models
from usuarios.models import Usuario
import json

# Create your models here.
class Trabajador(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    nivel = models.CharField(max_length=50, null=False)
    foto = models.ImageField('Foto de Trabajador', upload_to='trabajadores/', blank=True, null=True)
    descripcion = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return json.dumps({
            'nombre': self.nombre,
            'nivel': self.nivel,
            'foto': self.foto.name,
            'descripcion': self.descripcion,

        })
    
class Testimonio(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    comentario =  models.TextField(null=True)
    servicio = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
def __str__(self):
    return json.dumps({
        'user': self.user,
        'comentario': self.comentario,
        'servicio': self.servicio,
    })