from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    ci = models.CharField('Carnet de identidad', max_length=11, null=True)
    telefono = models.CharField('Télefono', max_length=15, null=True)
    direccion = models.TextField('Dirección particular', null=True)
    avatar = models.ImageField('Avatar para tu perfil', upload_to='avatares/', blank=True, null=True)
    
    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"
        
    def __str__(self) -> str:
        return self.username

class Notificaciones(models.Model):
    user = models.ForeignKey(Usuario, null=True, on_delete=models.CASCADE)
    leido = models.BooleanField(default=False, null=False)
    # mensaje = models.CharField(null=False, max_length=100)