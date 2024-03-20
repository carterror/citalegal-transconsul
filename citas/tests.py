from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from usuarios.models import Usuario
from django.test import TestCase, Client
from django.urls import reverse
import os

# Create your tests here.
class AdminTest(TestCase):
    def test_admin_site_login(self):
        response = self.client.get(reverse('admin:login'))
        self.assertEqual(response.status_code, 200)
        
class AdminIntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = Usuario.objects.create_superuser(
            'admin', 'admin@test.com', 'admin'
        )
        self.client.login(username='admin', password='admin')

    def test_admin_dashboard_access(self):
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200)
        
class AdminAcceptanceTest(StaticLiveServerTestCase, TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()
        cls.admin_user = Usuario.objects.create_superuser(
            'admin', 'admin@test.com', 'admin'
        )
        cls.selenium = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_admin_login_page(self):
        self.selenium.get(f'{self.live_server_url}/admin/')
        username_input = self.selenium.find_element(By.NAME, 'username')
        username_input.send_keys('admin')
        password_input = self.selenium.find_element(By.NAME, 'password')
        password_input.send_keys('admin')
        self.selenium.find_element(By.XPATH, '//button[@type="submit"]').click()

        # Verificar que estamos en la página del dashboard
        self.assertIn('<title>Administración del sitio | Cita-Legal Admin</title>', self.selenium.page_source)
