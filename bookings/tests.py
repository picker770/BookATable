from django.test import TestCase
from django.contrib.auth.models import User
from django.db import IntegrityError
from datetime import date, timedelta
from .models import Table, TimeSlot, Booking

# Create your tests here.

class TableModelTest(TestCase):
    """Test the Table model"""

    def test_create_table(self):
        table = Table.objects.create(
            table_number=1,
            capacity=4,
            is_active=True
        )
        self.assertEqual(table.table_number, 1)
        self.assertEqual(table.capacity, 4)
        self.assertTrue(table.is_active)

    def test_table_string_representation(self):
        """Test table __str__ method"""
        table = Table.objects.create(table_number=1, capacity=4)
        self.assertEqual(str(table), "Table 1 (4 Seats)")

class TimeSlotModelTest(TestCase):
    """Test the TimeSlot model"""

    def test_create_timeslot(self):
        """Test creating a time slot"""
        slot = TimeSlot.objects.create(start_time='19:00')
        self.assertEqual(slot.start_time, '19:00')

    def test_timeslot_string_representation(self):
        """Test time slot __str__ method"""
        slot = TimeSlot.objects.create(start_time='19:00')
        self.assertEqual(str(slot), "7:00 PM")

class BookingModelTest(TestCase):
    """"Test the Booking Model"""

    def setUp(self):
        """Create test data before each test"""
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.table = Table.objects.create(table_number=1, capacity=4)
        self.timeslot = TimeSlot.objects.create(start_time='19:00')

    def test_create_booking(self):
        """Test creating a booking"""
        booking = Booking.objects.create(
            user=self.user,
            table=self.table,
            time_slot=self.timeslot,
            date=date.today() + timedelta(days=1),
            number_of_guests=2
        )
        self.assertEqual(booking.status, 'confirmed')
        self.assertIsNotNone(booking.booking_reference)
        self.assertEqual(len(booking.booking_reference), 8)

    def test_booking_string_representation(self):
        """Test booking __str__ method"""
        booking = Booking.objects.create(
            user=self.user,
            table=self.table,
            time_slot=self.timeslot,
            date=date.today() + timedelta(days=1),
            number_of_guests=2
        )
        self.assertIn(booking.booking_reference, str(booking))
        self.assertIn('testuser', str(booking))

    def test_prevent_double_booking(self):
        """Test that same table/date/time cannot be booked twice"""
        booking = Booking.objects.create(
            user=self.user,
            table=self.table,
            time_slot=self.timeslot,
            date=date.today() + timedelta(days=1),
            number_of_guests=2
        )

        # Creating duplicate should raise ItegrityError
        with self.assertRaises(IntegrityError):
            booking = Booking.objects.create(
            user=self.user,
            table=self.table,
            time_slot=self.timeslot,
            date=date.today() + timedelta(days=1),
            number_of_guests=2
        )

        
