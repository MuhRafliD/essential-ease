from django.test import TestCase, Client
from .models import Product

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    def setUp(self):
        self.product_initiate = Product.objects.create(
            name = 'Aqua',
            amount = 50,
            description = 'minuman segar asli pegunungan',
            price = 500,
            category = 'Minuman',
        )
    
    def test_model_fields(self):
        product = Product.objects.get(id=self.product_initiate.id)
        self.assertEqual(product.name, 'Aqua')
        self.assertEqual(product.amount, 50)
        self.assertEqual(product.description, 'minuman segar asli pegunungan')
        self.assertEqual(product.price, 500)
        self.assertEqual(product.category, 'Minuman')