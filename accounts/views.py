from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    """Handle user registration"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
        else:
             # Form is invalid, return to registration page with errors
             return render(request, 'accounts/register.html', { 'form': form })
        
    else:
        # GET request - show empty registration form
        form = UserCreationForm()
        return render(request, 'accounts/register.html', {'form': form})
    
@login_required
def profile(request):
        """Display user profile page"""
        return render(request, 'accounts/profile.html')