from django.db import models
from django.template.defaultfilters import slugify
import json
from usuarios.models import Usuario

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    cuerpo = models.TextField()
    presentar = models.BooleanField(blank = True, null = False, default=True)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    publicado = models.DateTimeField(auto_now_add=True)
    foto = models.ImageField('Foto arti', upload_to='posts/', blank=True, null=True)


    def __str__(self):
        return json.dumps({
            'titulo': self.titulo,
            'cuerpo': self.cuerpo,
            'presentar': self.presentar,
            'foto': self.foto.name,
        })
   
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.titulo)

        super(Post, self).save(*args, **kwargs)