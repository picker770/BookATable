from django.test import TestCase
from .models import Category, MenuItem

# Create your tests here.

class CategoryModelTest(TestCase):
    """Test the Category model"""

    def test_create_category(self):
        """Test creating a category"""
        category = Category.objects.create(name='Starters')
        self.assertEqual(category.name, 'Starters')

    def test_category_string_representation(self):
        """Test category __str__ method"""
        category = Category.objects.create(name='Mains')
        self.assertEqual(str(category), 'Mains')

    def test_category_plural_name(self):
        """Test verbose_name_plural works"""
        self.assertEqual(str(Category._meta.verbose_name_plural), 'Categories')

class MenuItemModelTest(TestCase):
    """Test the MenuItem model"""

    def setUp(self):
        self.category = Category.objects.create(name='Starters')

    def test_create_menu_item(self):
        """Test creating a menu item"""
        item = MenuItem.objects.create(
            name='Garlic Bread',
            description='Toasted bread with garlic butter',
            price=4.50,
            category = self.category,
            is_available=True
        )
        self.assertEqual(item.name, 'Garlic Bread')
        self.assertEqual(item.price, 4.50)
        self.assertTrue(item.is_available)

    def test_menu_item_string_representation(self):
        """Test menu item __str__ method"""
        item = MenuItem.objects.create(
            name='Bruschetta',
            description='Tomatoes, basil, olive oil',
            price=5.50,
            category=self.category
        )
        self.assertEqual(str(item), 'Bruschetta - £5.50')

    def test_menu_item_filter_by_availability(self):
        """Test that unavailable items can be filtered"""
        item1 = MenuItem.objects.create(
            name='Available Dish',
            description='Test',
            price=10.00,
            category=self.category,
            is_available=True
        )
        item2 = MenuItem.objects.create(
            name='Unavailable Dish',
            description='Test',
            price=10.00,
            category=self.category,
            is_available=False
        )

        available_items = MenuItem.objects.filter(is_available=True)
        self.assertIn(item1, available_items)
        self.assertNotIn(item2, available_items)

    def test_menu_item_price_decimal(self):
        """Test price stores decimals correctly"""
        item = MenuItem.objects.create(
            name='Test Dish',
            description='Test',
            price=9.99,
            category=self.category
        )
        self.assertEqual(float(item.price), 9.99)
