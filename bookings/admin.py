from django.contrib import admin
from .models import Table, TimeSlot, Booking

# Register your models here.

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ['table_number', 'capacity', 'is_active']
    list_filter = ['capacity', 'is_active']
    search_fields = ['table_number']

@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ['start_time']
    ordering = ['start_time']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['booking_reference', 'user', 'date', 'time_slot', 'table', 'status']
    list_filter = ['status', 'date']
    search_fields = ['booking_reference', 'user__username']
    readonly_fields = ['booking_reference', 'created_at']
