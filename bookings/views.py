from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Booking, Table, TimeSlot
from .forms import BookingForm

# Create your views here.
@login_required
def create_booking(request):
    """Handle table booking creation"""
    available_tables = Table.objects.filter(is_active=True)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user

            # Get selected data
            selected_date = form.cleaned_data['date']
            selected_time_slot = form.cleaned_data['time_slot']
            num_guests = form.cleaned_data['number_of_guests']

            # Find suitable table
            suitable_tables = available_tables.filter(capacity__gte=num_guests)

            # Check which tables are available for this date and time
            available_table = None
            for table in suitable_tables:
                existing_booking = Booking.objects.filter(
                    table=table,
                    date=selected_date,
                    time_slot=selected_time_slot,
                    status='confirmed'
                ).exists()

                if not existing_booking:
                    available_table = table
                    break
            
            if available_table:
                booking.table = available_table
                booking.save()
                messages.success(request, f'Booking confirmed! Your reference number is {booking.booking_reference}')
                return redirect('booking_success', booking_id=booking.id)
            
            else:
                messages.error(request, 'No tables available for your selected date, time, and guest count. Please try different options.')
                return redirect('create_booking')
            
    else:
        form = BookingForm()

    context = {
        'form': form,
        'available_tables': available_tables,
    }
    return render(request, 'bookings/create_booking.html', context)

@login_required
def my_bookings(request):
    """Display user's bookings"""
    upcoming_bookings = Booking.objects.filter(
        user=request.user,
        date__gte=timezone.now().date(),
        status='confirmed'
    ).order_by('date', 'time_slot')
    
    past_bookings = Booking.objects.filter(
        user=request.user,
        date__lt=timezone.now().date(),
        status='confirmed'
    ).order_by('-date')
    
    cancelled_bookings = Booking.objects.filter(
        user=request.user,
        status='cancelled'
    ).order_by('-created_at')
    
    context = {
        'upcoming_bookings': upcoming_bookings,
        'past_bookings': past_bookings,
        'cancelled_bookings': cancelled_bookings,
    }
    return render(request, 'bookings/my_bookings.html', context)

@login_required
def cancel_booking(request, booking_id):
    """Cancel a booking"""
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    
    if booking.status == 'confirmed':
        booking.status = 'cancelled'
        booking.save()
        messages.success(request, f'Booking {booking.booking_reference} has been cancelled.')
    else:
        messages.error(request, 'This booking cannot be cancelled.')
    
    return redirect('my_bookings')

@login_required
def booking_success(request, booking_id):
    """Show booking confirmation"""
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    return render(request, 'bookings/booking_success.html', {'booking': booking})
