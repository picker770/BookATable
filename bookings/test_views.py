from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date, timedelta
from .models import Table, TimeSlot, Booking


class BookingViewsTest(TestCase):
    """Test the booking views"""

    def setUp(self):
        """Create test data before each test"""
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.table = Table.objects.create(table_number=1, capacity=4)
        self.timeslot = TimeSlot.objects.create(start_time='19:00')

    def test_create_booking_requires_login(self):
        """Test that unauthenticated users cannot book"""
        response = self.client.get(reverse('create_booking'))
        self.assertEqual(response.status_code, 302) # Redirects to login
        self.assertIn('login', response.url)

    def test_create_booking_page_loads_for_logged_in_user(self):
        """Test logged-in users can access booking page"""
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('create_booking'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/create_booking.html')

    def test_my_bookings_loads_for_logged_in_user(self):
        """Test uanuthenticated users cannot view bookings"""
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('my_bookings'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/my_bookings.html')

    def test_cancel_booking_requires_login(self):
        """Test unauthenticated users cannot cancel bookings"""
        response = self.client.get(reverse('cancel_booking', args=[1]))
        self.assertEqual(response.status_code, 302) # redirects to login


    