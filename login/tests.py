from django.test import TestCase
from .models import Customer
from .models import RoomManager
from booking.models import Booking, Rooms
import datetime

class CustomerTestCase(TestCase):

    def setUp(self):
        Customer.objects.create(username='virat',email='virat18@gmail.com',pin_code=798846,phone_no='7794173921')
        Customer.objects.create(username='dhoni',email='dhoni7@gmail.com',pin_code=790004,phone_no='9090009090')
    
    def test_customer_username(self):
        customer1=Customer.objects.get(phone_no='7794173921')
        customer2=Customer.objects.get(username='dhoni')
        self.assertEqual(customer1.username,'virat')
        self.assertEqual(customer2.username,'dhoni')
    
    def test_customer_email(self):
        customer1=Customer.objects.get(email='virat18@gmail.com')
        customer2=Customer.objects.get(username='dhoni')
        self.assertEqual(customer1.email,'virat18@gmail.com')
        self.assertEqual(customer2.email,'dhoni7@gmail.com')

class RoomManagerTestCase(TestCase):
    
    def setUp(self):
        RoomManager.objects.create(username='virat',email='virat18@gmail.com',phone_no='7794173921')
        RoomManager.objects.create(username='dhoni',email='dhoni7@gmail.com',phone_no='9090009090')
    
    def test_roomManager_username(self):
        manager1=RoomManager.objects.get(username='virat')
        manager2=RoomManager.objects.get(username='dhoni')
        self.assertEqual(manager1.username,'virat')
        self.assertEqual(manager2.username,'dhoni')
    
    def test_roomManager_email(self):
        manager1=RoomManager.objects.get(email='virat18@gmail.com')
        manager2=RoomManager.objects.get(email='dhoni7@gmail.com')
        self.assertEqual(manager1.email,'virat18@gmail.com')
        self.assertEqual(manager2.email,'dhoni7@gmail.com')
    
    def test_roomManager_phone(self):
        manager1=RoomManager.objects.get(phone_no='7794173921')
        manager2=RoomManager.objects.get(phone_no='9090009090')
        self.assertEqual(manager1.phone_no,'7794173921')
        self.assertEqual(manager2.phone_no,'9090009090')


