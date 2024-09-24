from django.db import models
import json
from usuarios.models import Usuario

# Create your models here.


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
    
    def __str__(self):
        return json.dumps({
            'disponible': self.disponible,
            'fecha': self.fecha.strftime('%Y-%m-%d'),
            'abogado': self.abogado,
        })
    
    
class Tramite(models.Model):
    codigo = models.CharField(max_length=10, null=False, unique=True)
    nombre = models.CharField(max_length=250)
    precio = models.DecimalField(decimal_places=2, max_digits=9)
    descripcion = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return json.dumps({
            'codigo' : self.codigo,
            'nombre' : self.nombre,
            'precio' : self.precio.as_integer_ratio(),
            'descripcion' : self.descripcion
        })
    
class Cita(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='clientes')
    legalizadora = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='legalizadoras')
    tramite = models.ForeignKey(Tramite, on_delete=models.CASCADE, related_name='tramites')
    fecha = models.ForeignKey(Disponible, on_delete=models.CASCADE, related_name='disponibles')

    cantidad_documentos = models.IntegerField('Documentos', null=True)
    lugar = models.CharField(max_length=250, null=True)
    motivo = models.TextField(null=True)
    estado = models.CharField(max_length=50, default='pending', choices=ESTADOS)

    created_at = models.DateTimeField('Creado', auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return str(self.created_at)