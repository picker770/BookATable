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

I have used the recommended [HTML W3C validator](https://validator.w3.org) to validate all of my HTML files.

| Page | URL | Status |
|------|-----|--------|
| Homepage | `https://bookatable-raja-2655b485c5d7.herokuapp.com/`| ✅ Pass |
| Menu | `https://bookatable-raja-2655b485c5d7.herokuapp.com/menu/`| ✅ Pass |
| Login | `https://bookatable-raja-2655b485c5d7.herokuapp.com/accounts/login/`| ✅ Pass |
| Register | `https://bookatable-raja-2655b485c5d7.herokuapp.com/accounts/register/`| ✅ Pass |
| Book a table | `https://bookatable-raja-2655b485c5d7.herokuapp.com/bookings/create/`| ✅ Pass |
| My Bookings | `https://bookatable-raja-2655b485c5d7.herokuapp.com/bookings/my-bookings/`| ✅ Pass |
| Profile | `https://bookatable-raja-2655b485c5d7.herokuapp.com/accounts/profile/`| ✅ Pass |

### HTML Code validation screenshots

| Homepage | ![](/static/docs/html-validaton-screenshots/home.png)|
| Menu | ![](/static/docs/html-validaton-screenshots/menu.png)|
| Login | ![](/static/docs/html-validaton-screenshots/login.png)|
| Register | ![](/static/docs/html-validaton-screenshots/register.png)|
| Book a table | ![](/static/docs/html-validaton-screenshots/create.png)|
| My Bookings | ![](/static/docs/html-validaton-screenshots/my-bookings.png)|
| Profile | ![](/static/docs/html-validaton-screenshots/profile.png)|


### CSS Validation

I have used the recommend [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate my CSS files.

| File | Link | Status |
|------|------|--------|
| `static/css/custom.css` | [Validate CSS ](https://jigsaw.w3.org/css-validator/validator?uri=https://bookatable-raja-2655b485c5d7.herokuapp.com/static/css/custom.css) | ✅ Pass |


---

## Lighthouse Testing (Chrome DevTools)

Lighthouse audits were run on the deployed Heroku site.

| Category | Score | Screenshot |
|----------|-------|------------|
| Performance | 99% | ![performance](/static/docs/lighthouse/performance.png) |
| Accessibility | 98% | ![performance](/static/docs/lighthouse/accessibility.png) |
| Best Practices | 77% | ![performance](/static/docs/lighthouse/bestpractices.png) |
| SEO | 100% | ![performance](/static/docs/lighthouse/seo.png) |

*(Scores may vary slightly by device/network)*

**Note:** Best Pracitces score of 77% is due to third-party cookies from external resources(unsplash hero images).

## Unit Testing Results

Django's built-in test framework was used for unit testing.

### Test files

| File | Tests | Description |
|------|-------|-------------|
| `bookings/tests.py`| 7 tests | Table, TimeSlot, Booking models, double-booking prevention |
| `bookings/test_views.py` | 4 tests | View access, login requirements |
| `menu/tests.py` | 7 tests | Category and MenuItem models |
| `accounts/tests.py`| 6 tests | Registration, login, profile access |

### Test Output

```
python manage.py test
Found 24 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
........................
----------------------------------------------------------------------
Ran 24 tests in 18.556s

OK
```

### What was Tested

* ✅ Table creation with capacity choices (2,4,6,8 seats)
* ✅ TimeSlot creation with time choices (5:00PM - 9:00 PM)
* ✅ Booking auto-generates 8-character reference number
* ✅ Double-booking prevention raises IntegerityError
* ✅ Unauthenticated users redirected from booking pages
* ✅ Menu item price formatting (2 decimal places)
* ✅ User registration with valid/invalid passwords

---

## Responsiveness Testing

Tested using Chrome DevTools on the following breakpoints:

| Device | Screen Width | Result |
|--------|--------------|--------|
| iphone SE | 375px | ✅ Fully responsive|
| iphone 12/13/14 | 390px | ✅ Fully responsive|
| ipad Mini | 768px | ✅ Fully responsive|
| ipad Air | 820px | ✅ Fully responsive|
| Desktop | 1024px+ | ✅ Fully responsive|
| Desktop | 1440px+ | ✅ Fully responsive|
| Desktop | 1920px+ | ✅ Fully responsive|

### Responsive Features Verified:
* ✅ Navigation bar collapses to hamburger menu on mobile
* ✅ Menu cards stack vertically on mobile (1 column)
* ✅ Menu cards display in 2 columns on desktop
* ✅ Booking form adjusts to full width on mobile
* ✅ Tables display in responsive grid
* ✅ Footer stacks columns on mobile
* ✅ Button sizes remain touch-friendly
* ✅ No horizontal scroll on any device

#### Sceenshots 

| Device/ View | Screenshot |
|--------------|------------|
| Mobile - Menu Page | ![](/static/docs/responsiveness/mobile-menu.png)|
| Tablet - Booking Form | ![](/static/docs/responsiveness/tablet-booking.png)|
| Desktop - Homepage | ![](/static/docs/responsiveness/desktop-home.png)|

---

## Browser Compatibility

| Browser | Screenshot | Result |
|---------|------------|--------|
| Chrome  | ![Chrome](/static/docs/browser-testing/chrome.png)| ✅ Work as expected |
| Edge    | ![Edge](/static/docs/browser-testing/edge.png)| ✅ Work as expected |
| Firefox  | ![Firefox](/static/docs/browser-testing/firefox.png)| ✅ Work as expected |
| Safari  | ![Safari](/static/docs/browser-testing/safari.png)| ✅ Work as expected |
| Opera  | ![Opera](/static/docs/browser-testing/opera.png)| ✅ Work as expected |

---

## Test Cases(Sample)

| Feature | Step(s) | Expected | Actual | Pass |
|---------|---------|----------|--------|------|
| User Registration | Fill form with valid data | Redirect to login, user created | As expectd | ✅ |
| User Login | Enter valid credentials | Redirect to home, navbar changes | As expected | ✅ |
| View Menu | Click "Menu" in navbar | All categories and items displayed | As expected | ✅ |
| Create Booking | Select date,time,guests,submit | Booking reference displayed | As expected | ✅ 
| My Bookings | Click "My Bookings" | Upcoming Bookings shown | As expected | ✅ |
| Cancel Booking | Click cancel button | Booking moves to cancelled section | As expected | ✅ |
| Double-Booking | Book same date/time twice | Different table assign or error shown | As expected | ✅ |
| Admin Access | visit /admin with superuser | Admin dashboard displays | As expected | ✅ |

---

## Accessibility Testing
Manual accessibility checks were performed:

| Test | Result |
|------|--------|
| Semantic HTML structure(header, nav, main, footer)| ✅ Pass |
| ARIA labels on icon-only links | ✅ Pass |
| Color contrast ratio (WCAG 2.1 AA) - 7.1:1 | ✅ Pass |
| Keyboard navigation(Tab, Shift+Tab, Enter) | ✅ Pass |
| Form labels associated with inputs | ✅ Pass |
| Heading hierarchy (h1,h2,h3) | ✅ Pass |
| Form labels associated with inputs | ✅ Pass |

---

## User Story Testing
### New Customers

| User Story | Test | Result |
|------------|------|--------|
| I want to view the menu without logging in | Visit /menu/ as guest | ✅ Menu fully visible |		
| I want to book a table easily | Click "Book a Table", fill form |	✅ Simple 4-field form |
| I want to choose date, time, and guest count |	Use booking form dropdowns |	✅ All options available |
| I want confirmation of my booking |	Submit booking |	✅ Reference number displayed |

### Returning Customers

| User Story | Test | Result |
|------------|------|---------|
|I want to log in quickly|	Use login form|	✅ Redirects to homepage|
|I want to view my upcoming bookings|	Click "My Bookings"|	✅ Upcoming section shows active bookings|
|I want to cancel a booking|	Click cancel button	|✅ Confirmation, moved to cancelled|
|I want to see my booking history|	View My Bookings page|	✅ Past and cancelled sections visible|

### Restaurant Owner (Admin)

|User Story|	Test|	Result|
|----------|--------|---------|
|I want to manage tables|	Admin → Tables → Add/Edit/|	✅ Full CRUD functionality|
|I want to manage time slots|	Admin → Time slots → Add/Edit/Delete|	✅ Full CRUD functionality|
|I want to view all bookings|	Admin → Bookings	|✅ All bookings visible with filters|
|I want to prevent double-booking|	Attempt to double-book|	✅ Constraint prevents it|

## Accessibility Needs

|User Story|	Test|	Result|
|----------|--------|---------|
|I want sufficient color contrast|	Check with contrast tool|	✅ 7.1:1 ratio passes WCAG|
|I want to navigate without a mouse|	Use Tab, Enter keys|	✅ Full keyboard navigation|
|I want screen reader compatible links|	Check aria-labels|	✅ Icon links have labels|


---

## Bugs and Fixes

