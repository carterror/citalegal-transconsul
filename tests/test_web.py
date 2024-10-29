from django.test import TestCase
from web.models import Testimonio, Trabajador
from usuarios.models import Usuario

class TrabajadorUnitTest(TestCase):
    def setUp(self):
        Trabajador.objects.create(
            nombre = 'Certifica',
            nivel = 'Ing.'
        )
    
    def test_model(self):
        post = Trabajador.objects.first()
        self.assertEqual(post.nombre, 'Certifica')

class TestimonioUnitTest(TestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create_superuser(username='admin', password='admin')

    
        Testimonio.objects.create(
            user = self.usuario,
            comentario = 'Lo mejor'
        )
    
    def test_model(self):
        testi = Testimonio.objects.first()
        self.assertEqual(testi.comentario, 'Lo mejor')
