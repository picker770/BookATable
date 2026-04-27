from django.shortcuts import render
from .models import Category, MenuItem

# Create your views here.


def menu_list(request):
    """Display all menu items grouped by category"""
    categories = Category.objects.all()
    menu_items = MenuItem.objects.filter(is_available=True)

    # Organize menu items by category
    menu_by_category = {}
    for category in categories:
        menu_by_category[category] = menu_items.filter(category=category)

    context = {
        'menu_by_category': menu_by_category,
    }
    return render(request, 'menu/menu_list.html', context)