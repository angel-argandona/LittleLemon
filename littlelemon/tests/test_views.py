from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
	def setUp(self):
		self.item1 = Menu.objects.create(title = "Ice Cream", price = 4, inventory = 100)
		self.item2 = Menu.objects.create(title = "Bruschetta", price = 7.50, inventory = 80)
		self.item3 = Menu.objects.create(title = "Grilled fish", price = 15, inventory = 35)

	def test_getall(self):
		menu_items = Menu.objects.all()
		serialized_items = MenuSerializer(menu_items, many = True)
		expected_output = [
      		{
				'id': self.item1.id,
				'title': 'Ice Cream',
				'price': '4.00',
				'inventory': 100
            },
        	{
				'id': self.item2.id,
				'title': 'Bruschetta',
				'price': '7.50',
				'inventory': 80
            },
        	{
				'id': self.item3.id,
				'title': 'Grilled fish',
				'price': '15.00',
				'inventory': 35
			}
        ]
		self.assertEqual(serialized_items.data, expected_output)