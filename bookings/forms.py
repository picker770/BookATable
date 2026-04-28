from django import forms
from .models import Booking, Table, TimeSlot
from datetime import date

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date', 'time_slot', 'number_of_guests', 'special_requests']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time_slot': forms.Select(attrs={'class': 'form-control'}),
            'special_requests': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placholder': 'Any dietary requirements or special requests?'}),
            }
        labels = {
            'date': 'Select Date',
            'time_slot': 'Select Time',
            'number_of_guests': 'Number of Guests',
            'special_requests': 'Special Requests (Optional)',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #Only show future dates
        self.fields['date'].widget.attrs['min'] = date.today().isoformat()

        # Limit time slots 
        self.fields['time_slot'].queryset = TimeSlot.objects.all()