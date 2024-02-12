from django.test import TestCase
from .models import Customer, Product, Order

class CustomerModelTest(TestCase):
    def test_string_representation(self):
        customer = Customer(name="John Doe")
        self.assertEqual(str(customer), customer.name)

class ProductModelTest(TestCase):
    def test_string_representation(self):
        product = Product(title="Camera")
        self.assertEqual(str(product), product.title)

class HomePageTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_uses_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')