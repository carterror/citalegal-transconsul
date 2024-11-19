from django.test import TestCase, Client
from blog.models import Post
from usuarios.models import Usuario
from django.urls import reverse
from django.db import IntegrityError

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

class LocalTestCase(TestCase):
    def setUp(self):
        # Configura el entorno de prueba
        # Se crea un cliente 
        self.client = Client()
        # Un usuario super admin
        self.usuario = Usuario.objects.create_superuser(username='admin', password='admin')
        # se crean los locales
        Post.objects.create(
            titulo = 'Post 1',
            cuerpo = 'Cuerpo 1',
            autor = self.usuario,
        )

        Post.objects.create(
            titulo = 'Post 2',
            cuerpo = 'Cuerpo 2',
            autor = self.usuario,
        )
                
    # def test_get_ok(self):
    #     self.client.login(username='admin', password='admin')
        
    #     # Obtener la URL de la vista
    #     url = reverse('blog')
    #     # Realizar la solicitud GET a la vista
    #     response = self.client.get(url)
    #     # Verificar que la respuesta es 200 OK son los estados Http
    #     self.assertEqual(response.status_code, 200)
    #     # Verificar que los usuarios estén en el contexto de la respuesta
    #     article_en_contexto = response.context['blogs']
    #     self.assertEqual(len(article_en_contexto), 2)
    #     # Verificar que los datos de los usuarios estén en el contenido de la respuesta
    #     self.assertContains(response, 'Post 1')
    #     self.assertContains(response, 'Post 2')