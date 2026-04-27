from django.shortcuts import render

# Create your views here.

def home(request):
    """Homepage view"""
    return render(request, 'core/home.html')
