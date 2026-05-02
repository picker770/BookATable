
import random
import string
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Generate random booking reference
def generate_booking_reference():
    """
    Generate random 8-character booking reference
    """
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

class Table(models.Model):
    TABLE_CAPACITIES = [
        (2, '2 Seats'),
        (4, '4 Seats'),
        (6, '6 Seats'),
        (8, '8 Seats'),
    ]

    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField(choices=TABLE_CAPACITIES)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Table {self.table_number} ({self.capacity} Seats)"
    
class TimeSlot(models.Model):
    TIME_CHOICES = [
        ('17:00', '5:00 PM'),
        ('18:00', '6:00 PM'),
        ('19:00', '7:00 PM'),
        ('20:00', '8:00 PM'),
        ('21:00', '9:00 PM'),
    ]

    start_time = models.CharField(max_length=5, choices=TIME_CHOICES, unique=True)

    def __str__(self):
        return self.get_start_time_display()
        
class Booking(models.Model):
     STATUS_CHOICES = [
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]
     
     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
     table = models.ForeignKey(Table, on_delete=models.CASCADE)
     time_slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
     date = models.DateField()
     number_of_guests = models.IntegerField()
     special_requests = models.TextField(blank=True, null=True)
     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='confirmed')
     booking_reference = models.CharField(max_length=10, unique=True, blank=True)
     created_at = models.DateTimeField(auto_now_add=True)

     class Meta:
         # Prevent double-booking: same table, same date, same time slot
         unique_together = ['table', 'date', 'time_slot']

     def save(self, *args, **Kwargs):
         if not self.booking_reference:
             self.booking_reference = generate_booking_reference()
         super().save(*args, **Kwargs)

     def __str__(self):
         return f"Booking {self.booking_reference} - {self.user.username} - {self.date} {self.time_slot}"
