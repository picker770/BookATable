from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.

class AccountsTest(TestCase):
    """Test user authentication"""

    def setUp(self):
        self.client = Client()

    def test_register_page_loads(self):
        """Test registration page loads"""
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')

    def test_user_registration_success(self):
        """Test creating a new user successfully"""
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'password1': 'TestPass123!',
            'password2': 'TestPass123!',
        }, follow=True)

        # Check user was created
        self.assertTrue(User.objects.filter(username='newuser').exists())

        # Check final page loads (could be 200 after redirect)
        self.assertEqual(response.status_code, 200)
        

    def test_user_registration_password_mismatch(self):
        """Test registration fails when passwords don't match"""
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'password1': 'TestPass123!',
            'password2': 'DifferentPass456!',
        })
        self.assertFalse(User.objects.filter(username='newuser').exists())
        self.assertEqual(response.status_code, 200)
    
    def test_login_page_loads(self):
        """Test login page loads"""
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')
    
    def test_profile_requires_login(self):
        """Test unauthenticated users cannot view profile"""
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)  
    
    def test_profile_loads_for_logged_in_user(self):
        """Test logged-in users can view profile"""
        User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/profile.html')
