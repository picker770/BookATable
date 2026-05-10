# Testing - BookATable Spice 

This document outlines the testing carried out for the BookATable Spice application to ensure correct functionality, responsive layout, database integrity, and code reliability. Both **automated** and **manual** testing approaches were used throughout development.

---

## Testing Approach

### Automated Testing


**Framework**: Django Test Framework (unittest)

**Test Files**:
- `bookings/tests.py`
- `bookings/test_views.py`
- `menu/tests.py`
- `accounts/tests.py`

**What is test automatically**:

- ✅ Table model creation and string representation
- ✅ TimeSlot model creation and display
- ✅ Booking model with auto-generated reference
- ✅ Double-booking prevention
- ✅ Menu item creation and availability filtering
- ✅ User registration and password validation
- ✅ View access control (login requirements)

### Manual Testing

**What is tested manually**:

- ✅ User experience and visual layout
- ✅ Real-world booking scenarios
- ✅ Double-booking prevention edge cases
- ✅ Cross-browser and cross-device compatibility
- ✅ Accessibility with screen readers
- ✅ Keyboard navigation
- ✅ Form validation and error messages

---

## What is Testing?

Testing is the process of evaluating a software application to ensure it behaves as expected, meets requirements, and is free from defects. In web development, testing helps verify that code works correctly across different browsers, devices, and user scenarios. Testing improves code quality, reduce bugs, and enhances user experience.

### Types of Testing

#### Unit Testing

**Definition:** Unit testing involves testing individual components or fucntions of the code in isolation to ensure each part works correctly on its own.

**In this project:**

- Each model is tested independentaly (Table, TimeSlot, Booking, MenuItem)
- Tests verify that models have correct fields, constraints, and string representations
- Django's TestCase framework is used to run unit tests automatically
- Double-booking prevention with `IntegrityError` assertion

#### Automated Testing

Automated testing uses scripts and testing frameworks to run tests automatically without human intervention. Tests can be run repeatedly, ensuring consistent results and saving time during development.

**In this project:**

- Django Test Framework is used for automated testing
- Tests run with a single command: `python manage.py test`
- 24 unit tests covering models, views, and forms

#### Manual Testing

Manual testing involves a human interacting with the application to verify functionality, usability, and visual appearance. It tests real-world scenarios that automated tests might missed.

**In this project:**

- Visual layout on different screen sizes
- User experience and ease of navigation
- Browser compatibility (Chrome, Firefox, Edge, Safari)
- Device testing (mobile, tablet , desktop)
- Booking flow verification
- Double-booking prevention in real scenarios

---

## Code Validation

### HTML Validation




