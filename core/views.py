from django.shortcuts import render

# Create your views here.

def home(request):
    """Homepage view"""
    return render(request, 'core/home.html')

def custom_404(request, exception):
    """Custom 404 error handler"""
    return render(request, '404.html', status=404)
