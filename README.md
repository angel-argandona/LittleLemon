Little Lemon restaurant website back-end:
Django, Django REST Framework and MySQL

API endpoints:
/restaurant/menu/
/restaurant/booking/tables

For proper testing, create a virtual environment, install the packages included in requirements.txt and create a .env file in the Django project's main directory with the following structure:

# Django settings
DEBUG = True
SECRET_KEY = 'YOUR SECRET KEY'

# MySQL Database settings
DB_ENGINE = 'django.db.backends.mysql'
DB_NAME = 'YOUR DB NAME'
DB_USER = 'YOUR USERNAME'
DB_PASSWORD = 'YOUR PASSWORD'
DB_HOST = 'localhost'
DB_PORT = '3306'

You can run the following command in your terminal to create your secret key:
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"