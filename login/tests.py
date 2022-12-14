from django.test import TestCase
from .models import Customer
from .models import RoomManager
from booking.models import Booking, Rooms
import datetime

class CustomerTestCase(TestCase):
    def setUp(self):
        Customer.objects.create(username='neha',email='neha@gmail.com',pin_code=799046,phone_no='9515721848')
        Customer.objects.create(username='ramya',email='ramya@gmail.com',pin_code=799046,phone_no='9491471297')
    def test_customer_username(self):
        # I am just trying to take different case to prove the point
        customer1=Customer.objects.get(phone_no='9515721848')
        customer2=Customer.objects.get(username='ramya')
        self.assertEqual(customer1.username,'neha')
        self.assertEqual(customer2.username,'ramya')
    def test_customer_email(self):
        customer1=Customer.objects.get(email='neha@gmail.com')
        customer2=Customer.objects.get(username='ramya')
        self.assertEqual(customer1.email,'neha@gmail.com')
        self.assertEqual(customer2.email,'ramya@gmail.com')

class RoomManagerTestCase(TestCase):
    def setUp(self):
        RoomManager.objects.create(username='neha',email='neha@gmail.com',phone_no='9515721848')
        RoomManager.objects.create(username='ramya',email='ramya@gmail.com',phone_no='9491471297')
    def test_roomManager_username(self):
        manager1=RoomManager.objects.get(username='neha')
        manager2=RoomManager.objects.get(username='ramya')
        self.assertEqual(manager1.username,'neha')
        self.assertEqual(manager2.username,'ramya')
    def test_roomManager_email(self):
        manager1=RoomManager.objects.get(email='neha@gmail.com')
        manager2=RoomManager.objects.get(email='ramya@gmail.com')
        self.assertEqual(manager1.email,'neha@gmail.com')
        self.assertEqual(manager2.email,'ramya@gmail.com')
    def test_roomManager_phone(self):
        manager1=RoomManager.objects.get(phone_no='9515721848')
        manager2=RoomManager.objects.get(phone_no='9491471297')
        self.assertEqual(manager1.phone_no,'9515721848')
        self.assertEqual(manager2.phone_no,'9491471297')


