# Django Ecommerce/Market
## About

Django Ecommerce is an unique marketplace focused on enabling users to buy/sell products directly or request/send quotes without any complicated or exhaustive process. This is the opensource version of a larger project.

### Features
1. User Panel
    1. User Management 
        - Sign Up
        - Log In
        - Email Password Reset
        - Email Verification
    1. Dashboard
    1. Item  
        - Search (Category / Name)
        - Buy Item
        - Request Quote
        - Orders
            - Placed By User
            - Placed By Customer
        - Quote
            - Placed By User
            - Placed By Customer
            - Upload Pdf
                - By Customer
                    - Purchase Order
                - By User/Seller 
                    - Quote 
                    - Invoice
                    - Delivery Receipt 
    1. Email Notifications: Enabled when `EMAIL_SEND = True` in `settings.py`
    1. SMS Notifications: Enabled when `SMS_SEND = True` in `settings.py`. (Pingsms API)[https://pypi.org/project/pingsms-api/]
    1. Multiple Addresses: User addresses. One address can be set as default.
    1. Multiple Inventories: Each inventory must have an address.
    1. Item Listing: Each item is listed by against an inventory with visibility Public/Private.
    1. Shopping Cart
        - Checkout
        - TODO: Payment
    1. TODO: Chats and Notifications

1. Admin Panel
    1. Item Types
    1. Items
    1. Weight Groups
    1. Addresses
    1. Inventories
    1. Listings
    1. Orders
    1. Quotes
    1. Shopping Carts


## Installation
### Download the project
```bash
git clone https://github.com/sa1if3/django_ecommerce
``` 
or 

[Download ZIP](https://github.com/sa1if3/django_ecommerce/archive/refs/heads/main.zip)

### Set Environment 
Create a Virtual Environment
```bash
virtualenv venv
```

Activate Virtual Environment
```bash
source venv/bin/activate
```

Download Prequisites using requirements.txt
```bash
pip install -r requirements.txt
```

Deactivate Virtual Environment
```bash
deactivate
```

### Async Tasks using Celery and Redis
Install Redis in Ubuntu 20.04 by following this [tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-18-04)

In `settings.py` set the following variables. Change according to your use-case.

```python
BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Kolkata'
```

Activate Virtual Environment
```bash
source venv/bin/activate
```

Run Celery worker
```bash
celery -A django_ecommerce  worker -l info
```

[Note: In production this command can be put in Supervisor]

### Debug Toolbar
If you are interested in using the debug toolbar make sure to change your `settings.py` file with appropriate IP.

```python
DEBUG = True

INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]
```
### Migrate Database
The project uses PostgreSQL. Make sure your `settings.py` is set to correct credential.
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'farmersmarket',
        'USER': 'farmersmarketuser',
        'PASSWORD': 'fkfQbfu6gnhGt',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

Section A of my [tutorial](https://techflow360.com/how-to-build-django-rest-api-with-oauth-2-0/) covers the setting up a server part for Django development.

Run

```bash
python manage.py makemigrations
```
Followed by

```bash
python manage.py migrate
```

### Create a superuser
A superuser is required to access the admin panel located at `/accounts`

```bash
python manage.py createsuperuser
```
### Collect static
In case static files don't run properly simply run

```bash
python manage.py collectstatic
```

## Run Development Server
To start the project simply run the server with this command inside activated virtual environment.
```bash
python manage.py runserver
``` 

## First Run and Initial Data
### Admin Section
Go to `http://yourdomain.com/accounts` and log in as superuser. The admin needs to setup some initial data which restricts the user to sell items from the given category only. Enter data in the following order
1. Create Item Types: Type of item being sold
![Item Type](https://github.com/sa1if3/django_ecommerce/blob/main/Screenshots/item_type.PNG?raw=true)
1. Create Items : Each Item has an item type
![Item](https://github.com/sa1if3/django_ecommerce/blob/main/Screenshots/items.PNG?raw=true)
3. Create Weight Groups: Used during listing, quote request and orders
![Weight Group](https://github.com/sa1if3/django_ecommerce/blob/main/Screenshots/weight_group.PNG?raw=true)

### User Section
A seller also needs to setup some initial data to list their items.
1. Create Address: Used for Inventory and invoices
1. Create Inventory: Used for Listing items. The name is showed to buyer too.

1. Create Listing: List items for personal use view status as `Private` or for public to view and purchase by setting the view status as `Public`. If all the items of a listing were sold off the listing becomes automatically private and the seller is notified via email. The seller cannot search for their own listings.
## Screenshots
<table>
  <tr>
    <td>First Screen Page</td>
     <td>Holiday Mention</td>
     <td>Present day in purple and selected day in pink</td>
  </tr>
  <tr>
    <td><img src="screenshots/Screenshot_1582745092.png" width=270 height=480></td>
    <td><img src="screenshots/Screenshot_1582745125.png" width=270 height=480></td>
    <td><img src="screenshots/Screenshot_1582745139.png" width=270 height=480></td>
  </tr>
 </table>
## Theme and Images
[AdminLTE](https://adminlte.io/themes/v3/)

[unDraw](https://undraw.co/illustrations)

[pixabay](https://pixabay.com/)
