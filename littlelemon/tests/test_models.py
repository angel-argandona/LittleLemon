from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_Menu_item(self):
        item = Menu.objects.create(title = "Ice Cream", price = 4, inventory = 100)
        self.assertEqual(str(item), "Ice Cream: 4")