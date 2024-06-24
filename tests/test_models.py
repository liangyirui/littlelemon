from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title='IceCream', price=5.50, inventory=10)
        TestCase.assertEqual(item, 'IceCream : 5.50')