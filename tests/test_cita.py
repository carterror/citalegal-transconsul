from django.test import TestCase
from citas.models import Cita, Tramite, Disponible
from usuarios.models import Usuario
from datetime import datetime

class DisponibleUnitTest(TestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create_superuser(username='admin', password='admin')

        self.fecha = datetime.now()

        Disponible.objects.create(
            fecha = self.fecha,
            disponible = 1
        )
    
    def test_model(self):
        post = Disponible.objects.first()
        self.assertEqual(post.fecha, self.fecha)

class CitaUnitTest(TestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create_superuser(username='admin', password='admin')

    
        ttramite = Tramite.objects.create(
            codigo = 'A122',
            nombre = 'Tramite 1',
            precio = 100
        )

        tfecha = Disponible.objects.create(
            fecha = datetime.now(),
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