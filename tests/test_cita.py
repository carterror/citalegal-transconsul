from django.test import TestCase, Client
from citas.models import Cita, Tramite, Disponible
from usuarios.models import Usuario
from datetime import datetime, timezone
from django.urls import reverse

class DisponibleUnitTest(TestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create_superuser(username='admin', password='admin')

        self.fecha = datetime.now(tz=timezone.utc)

        Disponible.objects.create(
            fecha = self.fecha,
            disponible = 1
        )
    
    def test_model(self):
        post = Disponible.objects.first()
        self.assertEqual(post.disponible, 1)

class CitaUnitTest(TestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create_superuser(username='admin', password='admin')

    
        ttramite = Tramite.objects.create(
            codigo = 'A122',
            nombre = 'Tramite 1',
            precio = 100
        )

        tfecha = Disponible.objects.create(
            fecha = datetime.now(tz=timezone.utc),
            disponible = 1
        )

        Cita.objects.create(
            cliente = self.usuario,
            legalizadora = self.usuario,
            fecha = tfecha,
            tramite = ttramite
        )
    
    def test_model(self):
        cita = Cita.objects.first()
        self.assertEqual(cita.estado, 'pending')

class TramiteUnitTest(TestCase):
    def setUp(self):
        
        Tramite.objects.create(
            codigo = 'A122',
            nombre = 'Tramite 1',
            precio = 100
        )
    
    def test_model(self):
        post = Tramite.objects.first()
        self.assertEqual(post.codigo, 'A122')

class LocalTestCase(TestCase):
    def setUp(self):
        # Configura el entorno de prueba
        # Se crea un cliente 
        self.client = Client()
        # Un usuario super admin
        self.usuario = Usuario.objects.create_superuser(username='admin', password='admin')
        # se crean los locales
        Tramite.objects.create(
            codigo = 'A123',
            nombre = 'Tramite 1',
            precio = 100
        )
        Tramite.objects.create(
            codigo = 'A122',
            nombre = 'Tramite 2',
            precio = 100
        )
    
                
    # def test_get_ok(self):
    #     self.client.login(username='admin', password='admin')
        
    #     # Obtener la URL de la vista
    #     url = reverse('tramite')
    #     # Realizar la solicitud GET a la vista
    #     response = self.client.get(url)
    #     # Verificar que la respuesta es 200 OK son los estados Http
    #     self.assertEqual(response.status_code, 200)
    #     # Verificar que los usuarios estén en el contexto de la respuesta
    #     article_en_contexto = response.context['tramites']
    #     self.assertEqual(len(article_en_contexto), 2)
    #     # Verificar que los datos de los usuarios estén en el contenido de la respuesta
    #     self.assertContains(response, 'Post 1')
    #     self.assertContains(response, 'Post 2')