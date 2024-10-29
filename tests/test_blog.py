from django.test import TestCase
from blog.models import Post
from usuarios.models import Usuario

class BlogUnitTest(TestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create_superuser(username='admin', password='admin')

        Post.objects.create(
            titulo = 'Post 1',
            cuerpo = 'Cuerpo 1',
            autor = self.usuario,
        )
    
    def test_model(self):
        # recuperamos el primer objeto de la base de datos 
        post = Post.objects.first()
        # verificamos que tenga como nombre local
        self.assertEqual(post.titulo, 'Post 1')