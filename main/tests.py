from django.test import TestCase, Client
from .models import Item

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    def setUp(self):
        self.item_initiate = Item.objects.create(
            name = 'Aqua',
            amount = 50,
            description = 'minuman segar asli pegunungan',
            price = 500,
            category = 'Minuman',
        )
    
    def test_model_fields(self):
        item = Item.objects.get(id=self.item_initiate.id)
        self.assertEqual(item.name, 'Aqua')
        self.assertEqual(item.amount, 50)
        self.assertEqual(item.description, 'minuman segar asli pegunungan')
        self.assertEqual(item.price, 500)
        self.assertEqual(item.category, 'Minuman')