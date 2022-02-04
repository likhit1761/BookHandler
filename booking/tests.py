from django.test import TestCase,Client
from booking.views import book
from .models import Books
from .models import Booking
from login.models import Customer, BookManager
import datetime
from django.urls import reverse

class BooksTestCases(TestCase):
    def setUp(self):
        BookManager.objects.create(username='vivek')
        manager=BookManager.objects.get(username='vivek')
        Books.objects.create(manager=manager,book_no=300,book_type='Deluxe',price=3000,is_available=True,no_of_days_advance=10,start_date='2020-03-20')
        Books.objects.create(manager=manager,book_no=301,book_type='Super Deluxe',price=5000,is_available=True,no_of_days_advance=15,start_date='2020-03-26')

    def test_book_no(self):
        book1 = Books.objects.get(book_no='300')
        book2 = Books.objects.get(book_no='301')
        self.assertEqual(book1.book_no, '300')
        self.assertEqual(book2.book_no, '301')

    def test_book_type(self):
        book1 = Books.objects.get(book_type='Deluxe')
        book2 = Books.objects.get(book_type='Super Deluxe')
        self.assertEqual(book1.book_type, 'Deluxe')
        self.assertEqual(book2.book_type, 'Super Deluxe')
    
    def test_price(self):
        book1 = Books.objects.get(price=3000)
        book2 = Books.objects.get(price=5000)
        self.assertEqual(book1.price, 3000)
        self.assertEqual(book2.price, 5000)

class BookingTestCases(TestCase):
    def setUp(self):
        BookManager.objects.create(username='rahul')
        manager=BookManager.objects.get(username='rahul')
        Customer.objects.create(username='vivek',pin_code=799046)
        Customer.objects.create(username='vikas',pin_code=799046)
        Books.objects.create(book_no='300',no_of_days_advance=10,start_date='2020-03-09',manager=manager)
        user=Customer.objects.get(username='vivek')
        user1=Customer.objects.get(username='vikas')
        book=Books.objects.get(book_no='300')
        Booking.objects.create(user_id=user,book_no=book,amount=10000,start_day='2020-03-10',end_day='2020-03-10')
        Booking.objects.create(user_id=user1,book_no=book,amount=5000,start_day='2020-03-26',end_day='2020-03-28')

    def test_booking_username(self):
        user=Customer.objects.get(username='vivek')
        booking1 = Booking.objects.get(user_id=user)
        user1=Customer.objects.get(username='vikas')
        booking2 = Booking.objects.get(user_id=user1)
        self.assertEqual(booking1.user_id.username, 'vivek')
        self.assertEqual(booking2.user_id.username, 'vikas')
    
    def test_booking_amount(self):
        booking1 = Booking.objects.get(amount=10000)
        booking2 = Booking.objects.get(amount=5000)
        self.assertEqual(booking1.amount, 10000)
        self.assertEqual(booking2.amount, 5000)
    
    def test_booking_BookManager(self):
        booking = Booking.objects.get(amount=5000)
        self.assertEqual(booking.book_no.manager.username, 'rahul')

class IndexPageViewTest(TestCase):
    def setUp(self):
        self.client=Client()
        self.index_url=reverse('index')

    def test_index_view(self):
        response=self.client.get(self.index_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'booking/index.html')