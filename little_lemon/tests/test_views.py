from django.test import TestCase
from restaurant.models import Menu


# class MenuViewTest(TestCase):
#     def setup(self):
#         i1 = Menu.objects.create(title="IceCream", price=30, inventory=80)
#         # i2 = Menu.objects.create(title="Fruit Salad", price=50, inventory=100)
#         # i3 = Menu.objects.create(title="Pizza", price=80, inventory=50)

#         return [i1] #, i2, i3]
    

#     def test_getall(self):
#         items = self.setup()
#         response = self.client.get('http://127.0.0.1:8000/restaurant/menu/').json()
#         for i, item in enumerate(items):
#             for key in item.objects.values():
#                 self.assertEqual(key, response[i])
